#  Midnite Take Home
from flask import Flask, request, jsonify
import time

app = Flask(__name__)
# to store user activities
user_actions = {}

def check_alerts(user_action, amount, user_id, timestamp):
    alerts = []
    # check previous actions
    actions = user_actions[user_id]
    # store current actions
    actions.append((user_action, amount, timestamp))

    # Codes
    # Code 1100: A withdrawal amount over 100
    if actions[0] == 'withdraw' and actions[1] > 100:
        alerts.append(1100)
        
    # Code 30: The user makes 3 consecutive withdrawals
    if len(actions) >= 3 and (all[0] == 'withdraw' for a in actions[-3:]):
        alerts.append(30)

    # store the deposits 
    deposits = []
    # Code 300: The user makes 3 consecutive deposits where each one is larger than the previous deposit (withdrawals in between deposits can be ignored).
    for action in reversed(actions):
        if action[0] == 'deposit':
            deposits.append(action[1])

    if len(deposits) == 3 and deposits[2] > deposits[1] > deposits[0]:
        alerts.append(300)

    # Code 123: The total amount deposited in a 30-second window exceeds 200
    for act in actions:
        if act[0] == 'deposit' and timestamp <= 30 and sum(act[1]):
            alerts.append(123)

    return alerts

@app.route('/event', methods=['POST'])
def event():
    # convert the data to json
    data = request.json
    user_id = data['user_id']
    user_action = data['type']
    amount = float(data['amount'])
    timestamp = int(data['time'])
    
    # Check for alerts
    alert_codes = check_alerts(user_id, user_action, amount, timestamp)
    
    response = {
        "alert": bool(alert_codes),
        "alert_codes": alert_codes,
        "user_id": user_id
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
    