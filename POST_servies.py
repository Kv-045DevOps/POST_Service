from flask import Flask, jsonify, request
from requests import post
import json
#import os

app = Flask(__name__)
# link = str(os.getenv("DB_URL"))
link = "reqres.in/api/users"


@app.route('/posting', methods=['POST'])
def posting():
    def send_json1(sendjson1):
        # department send function
        sendjson1 = post("https://" + link + ":5001", json=sendjson1, headers={"Content-type": "application/json"})
        print(sendjson1.text)

    def send_json2(sendjson2):
        # Team send function
        sendjson2 = post("https://" + link + ":5002", json=sendjson2, headers={"Content-type": "application/json"})
        print(sendjson2.text)

    def send_json3(sendjson3):
        # Employee send function
        sendjson3 = post("https://" + link + ":5003", json=sendjson3, headers={"Content-type": "application/json"})
        print(sendjson3.text)

    def json_count(little_json):
        # Check null in json function
        len_keys = len(little_json)
        len_value = 0
        for i in little_json:
            n = little_json[i]
            if n == None:
                len_value = 0
            else:
                len_value += 1

        if len_value == len_keys:
            return True
        else:
            return False

    datajson = request.data
    data = json.loads(datajson)
    msg = "Successfully sent"

    for i in data:
        if i == "department":
            Department = data["department"]
            if Department == None:
                pass
            else:
                if json_count(Department) == True:
                    send_json1(Department)
                else:
                    msg = "Fill in all the fields"

        elif i == "team":
            Team = data["team"]
            if Team == None:
                pass
            else:
                if json_count(Team) == True:
                    send_json2(Team)
                else:
                    msg = "Fill in all the fields"

        elif i == "employee":
            Employee = data["employee"]
            if Employee == None:
                pass
            else:
                if json_count(Employee) == True:
                    send_json3(Employee)
                else:
                    msg = "Fill in all the fields"
        else:
            pass
    return jsonify(msg)

    # Example json: {"department": {"name": "1"}, "team": {"depart_id": "1", "name": "1", "manager_id": "1"}, "employee": {"team_id": "1", "name": "1", "sname": "1", "exp": "1", "position": "1", "salary": "1", "coefficient": "1"}}


if __name__ == '__main__':
    app.run(debug=True)
