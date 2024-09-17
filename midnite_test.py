#  Take Home
from flask import Flask, request, jsonify
import time

app = Flask(__name__)
# to store user activities
user_actions = {}

def check_alerts(user_action, amount, user_id, timestamp):
    alerts = []
    
    # Initialize user actions if not present
    if user_id not in user_actions:
        user_actions[user_id] = []
    actions = user_actions[user_id]
    
    # Store current action
    actions.append((user_action, amount, timestamp))

    # Code 1100: A withdrawal amount over 100
    if actions[-1][0] == 'withdraw' and actions[-1][1] > 100:
        alerts.append(1100)
        
    # Code 30: The user makes 3 consecutive withdrawals
    if len(actions) >= 3 and all(a[0] == 'withdraw' for a in actions[-3:]):
        alerts.append(30)

    # Store deposits for further checks
    deposits = []
    # Code 300: The user makes 3 consecutive deposits where each is larger than the previous
    for action in reversed(actions):
        if action[0] == 'deposit':
            deposits.append(action[1])

    if len(deposits) >= 3 and deposits[0] < deposits[1] < deposits[2]:
        alerts.append(300)

    # Code 123: The total amount deposited in a 30-second window exceeds 200
    total_deposit = 0
    for act in actions:
        if act[0] == 'deposit' and timestamp - act[2] <= 30:
            total_deposit += act[1]
    if total_deposit > 200:
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
    alert_codes = check_alerts(user_action, amount, user_id, timestamp)
    
    response = {
        "alert": bool(alert_codes),
        "alert_codes": alert_codes,
        "user_id": user_id
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
