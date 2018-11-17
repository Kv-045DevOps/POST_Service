from flask import Flask, jsonify, request
from requests import post
import json

app = Flask(__name__)

@app.route('/posting', methods=['POST'])
def posting():
    data = request.data
    dataDict = json.loads(data)

    def send_json1(sendjson1):
        sendjson1 = post("https://reqres.in/api/users:5001", json=sendjson1, headers={"Content-type": "application/json"})
        print(sendjson1.text)
    def send_json2(sendjson2):
        sendjson2 = post("https://reqres.in/api/users:5002", json=sendjson2, headers={"Content-type": "application/json"})
        print(sendjson2.text)
    def send_json3(sendjson3):
        sendjson3 = post("https://reqres.in/api/users:5003", json=sendjson3, headers={"Content-type": "application/json"})
        print(sendjson3.text)

    if "department" in dataDict and dataDict["department"]:
        data2send = {}
        for key in dataDict["department"]:
            data2send[key] = dataDict["department"][key]
            send_json1(data2send)
    elif "team" in dataDict and dataDict["team"]:
        data2send = {}
        for key in dataDict["team"]:
            data2send[key] = dataDict["team"][key]
            send_json2(data2send)
    elif "employee" in dataDict and dataDict["employee"]:
        data2send = {}
        for key in dataDict["employee"]:
            data2send[key] = dataDict["employee"][key]
            send_json3(data2send)
    else:
        pass

    # for i in dataDict:
    #     if i == "department":
    #         Department = dataDict["department"]
    #         send_json1(Department)
    #     elif i == "team":
    #         Team = dataDict["team"]
    #         send_json2(Team)
    #     elif i == "employee":
    #         Employee = dataDict["employee"]
    #         send_json3(Employee)
    #     else:
    #         pass


    # Department = dataDict["department"]
    # Team = dataDict["team"]
    # Employee = dataDict["employee"]

    # send_json1(Department)
    # send_json2(Team)
    # send_json3(Employee)

    return jsonify(dataDict)


if __name__ == '__main__':
    app.run(debug=True)