from flask import Flask, request, jsonify
from dapr.clients import DaprClient
import json
import logging
from flask_cors import CORS
import os
from azure.servicebus import ServiceBusClient, ServiceBusMessage

sb_connstring = os.getenv("SB_CONNSTRING")  # localhost or sqledge (container name)
sb_queuename = os.getenv("SB_QUEUENAME")  # whatever db

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)


def send_single_message(sender):
    message = ServiceBusMessage("Single Picture")
    sender.send_messages(message)
    print("Sent a single picture")


def send_a_list_of_messages(sender):
    messages = [ServiceBusMessage("List of pictures") for _ in range(5)]
    sender.send_messages(messages)
    print("Sent a list of 5 pictures")


servicebus_client = ServiceBusClient.from_connection_string(conn_str=sb_connstring, logging_enable=True)


@app.route('/room/leave', methods=['POST'])
def leave():

    logging.basicConfig(level=logging.INFO)
    team = request.get_json()

    with DaprClient() as client:
        # Publish an event/message using Dapr PubSub
        result = client.publish_event(
            pubsub_name='teampubsub',
            topic_name='teams',
            data=json.dumps(team),
            data_content_type='application/json',
        )

    with servicebus_client:
        sender = servicebus_client.get_queue_sender(queue_name=sb_queuename)
        with sender:
            send_single_message(sender)
            send_a_list_of_messages(sender)

    logging.info('Published data: ' + json.dumps(team))

    return jsonify({'status': 'success'}), 201


@app.route('/room/purge')
def purge():
    logging.info('Purging images from the queue')
    with servicebus_client:
        receiver = servicebus_client.get_queue_receiver(queue_name=sb_queuename, max_wait_time=5)
        with receiver:
            for msg in receiver:
                print("Received: " + str(msg))
                receiver.complete_message(msg)

    return jsonify({'status': 'success'}), 201


@app.route('/room/ping')
def ping():
    return jsonify({'reply': 'pong'}), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)
