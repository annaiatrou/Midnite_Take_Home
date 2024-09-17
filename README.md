# README.md

# clone the repository
git clone https://github.com/your-username/event-alerts-api.git
cd event-alerts-api

# run the flask server 
python3 midnite_test.py 

# test the API
curl -X POST http://127.0.0.1:5000/event \
-H "Content-Type: application/json" \
-d '{"type": "deposit", "amount": "150", "user_id": 1, "time": 162}"'

