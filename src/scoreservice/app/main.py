from flask import Flask, request, jsonify
from cloudevents.http import from_http
import json
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)


# Register Dapr pub/sub subscriptions
@app.route('/dapr/subscribe', methods=['GET'])
def subscribe():
    logging.basicConfig(level=logging.INFO)
    subscriptions = [{
        'pubsubname': 'teampubsub',
        'topic': 'teams',
        'route': '/score/teams'
    }]
    print('Dapr pub/sub is subscribed to: ' + json.dumps(subscriptions))
    logging.info('Dapr pub/sub is subscribed to: ' + json.dumps(subscriptions))

    return jsonify(subscriptions)


# Dapr subscription in /dapr/subscribe sets up this route
@app.route('/score/teams', methods=['POST'])
def orders_subscriber():
    event = from_http(request.headers, request.get_data())
    print('Subscriber received escape room score from: : %s' % event.data['team'], flush=True)
    logging.info('Subscriber received escape room score from: ' + event.data['team'])
    return json.dumps({'success': True}), 200, {
        'ContentType': 'application/json'}


@app.route('/score/ping')
def ping():
    return jsonify({'reply': 'pong'}), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5006)
