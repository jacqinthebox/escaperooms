from flask import Flask, request, jsonify
from cloudevents.http import from_http
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Register Dapr pub/sub subscriptions
@app.route('/dapr/subscribe', methods=['GET'])
def subscribe():
    subscriptions = [{
        'pubsubname': 'teampubsub',
        'topic': 'teams',
        'route': '/score/teams'
    }]
    print('Dapr pub/sub is subscribed to: ' + json.dumps(subscriptions))
    return jsonify(subscriptions)


# Dapr subscription in /dapr/subscribe sets up this route
@app.route('/score/teams', methods=['POST'])
def orders_subscriber():
    event = from_http(request.headers, request.get_data())
    print('Subscriber received : %s' % event.data['team'], flush=True)
    return json.dumps({'success': True}), 200, {
        'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5006)
