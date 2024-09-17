# README.md

# clone the repository
git clone https://github.com/your-username/event-alerts-api.git\
cd event-alerts-api

# run the flask server 
python3 midnite_test.py 

# test the API
To test the API, using postman

1) Create a New Request:

    Click the "New" button on the top left, then select "HTTP Request".\
    Set the Request Type to POST and in the URL field, enter your API endpoint: http://127.0.0.1:5000/event.\

2) Click on the "Headers" tab.
    
    Under the Key column, add the following:
    Key: Content-Type
    Value: application/json
    This header is important as it tells the server that you're sending JSON data.

3) Enter the JSON Body:

    Click on the "Body" tab, select the "raw" and select JSON as the format.
    In the text area, enter an example JSON payload (the request body)
    example:
     {
 
        "type": "deposit",
        "amount": "42.00",
        "user_id": 1,
        "time": 10

     }

4) Send the Request

5) Check response under the "Body" tab

