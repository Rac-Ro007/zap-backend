import json
from flask import Flask, jsonify, request
import time
from zapv2 import ZAPv2
from zap_functions import connection, attack_target, fetch_alerts;

app = Flask(__name__)

zap = connection()

@app.route('/', methods=['GET'])
def health_probe():
    return 'Server is Up & Running', 200

@app.route('/attack-target/', methods=['GET'])
def post_attack():
    global zap
    # target = json.loads(request.data)
    target = request.args.get('target')
    if not target:
        return jsonify({ 'error': 'Need Target to launch an Attack' }), 400
    
    return jsonify(attack_target(target, zap)), 200

@app.route('/get_alerts', methods=['GET'])
def fetch_target_alerts():
    global zap
    try:
        return jsonify(fetch_alerts(zap)), 200
    except Exception as e:
        return e

if __name__ == '__main__':
   app.run(port=5000)