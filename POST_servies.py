from flask import Flask, jsonify, request
from requests import post
import json

app = Flask(__name__)

@app.route('/posting', methods=['POST'])
def posting():

    def send_json1(sendjson1):
        sendjson1 = post("https://127.0.0.1:5002/depart", json=sendjson1, headers={"Content-type": "application/json"})
        print(sendjson1.text)
    def send_json2(sendjson2):
        sendjson2 = post("https://127.0.0.1:5002/team", json=sendjson2, headers={"Content-type": "application/json"})
        print(sendjson2.text)
    def send_json3(sendjson3):
        sendjson3 = post("https://127.0.0.1:5002/users", json=sendjson3, headers={"Content-type": "application/json"})
        print(sendjson3.text)

    datajson = request.data
    data = json.loads(datajson)

    for i in data:
        if i == "department":
            Department = data["department"]
            if Department == None:
                pass
            else:
                send_json1(Department)
        elif i == "team":
            Team = data["team"]
            if Team == None:
                pass
            else:
                send_json2(Team)
        elif i == "employee":
            Employee = data["employee"]
            if Employee == None:
                pass
            else:
                send_json3(Employee)
        else:
            pass

    """{"department": {"name": "1"}, "team": {"depart_id": "1", "name": "1", "manager_id": "1"}, "employee": {"team_id": "1", "name": "1", "sname": "1", "exp": "1", "position": "1", "salary": "1", "coefficient": "1"}}"""


    """ version for another format json:
    # data = request.get_json()
    # Department = data[0]
    # Team = data[1]
    # Employee = data[2]
    
    [{"department":{"name": "Ben"}},{"team":{"depart_id":"1","name":"Viktor","manager_id":"5"}},{"employee":{"team_id":"11","name":"Dmitriy","sname":"Dimin","exp":"3","position":"Manager","salary":"1500","coefficient":"1"}}]"""

    return ""
    #jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)