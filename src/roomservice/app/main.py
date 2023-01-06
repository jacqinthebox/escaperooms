from flask import Flask, request, jsonify
from dapr.clients import DaprClient
import json
import logging
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)


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

    logging.info('Published data: ' + json.dumps(team))

    return jsonify({'status': 'success'}), 201


@app.route('/room/ping')
def ping():
    return jsonify({'status': 'success'}), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)
