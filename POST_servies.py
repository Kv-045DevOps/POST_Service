from flask import Flask, jsonify, request
from requests import post

app = Flask(__name__)

@app.route('/posting', methods=['POST'])
def posting():
    data = request.get_json()
    Department = data[0]
    Team = data[1]
    Employee = data[2]

    def send_json1(sendjson1):
        sendjson1 = post("https://reqres.in/api/users:5001", json=sendjson1, headers={"Content-type": "application/json"})
        print(sendjson1.text)
    def send_json2(sendjson2):
        sendjson2 = post("https://reqres.in/api/users:5002", json=sendjson2, headers={"Content-type": "application/json"})
        print(sendjson2.text)
    def send_json3(sendjson3):
        sendjson3 = post("https://reqres.in/api/users:5003", json=sendjson3, headers={"Content-type": "application/json"})
        print(sendjson3.text)
    send_json1(Department)
    send_json2(Team)
    send_json3(Employee)

    return jsonify(Department, Team, Employee)


if __name__ == '__main__':
    app.run(debug=True)