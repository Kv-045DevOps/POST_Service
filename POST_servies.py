from flask import Flask, jsonify, request
from requests import post

app = Flask(__name__)

@app.route('/posting', methods=['POST'])
def posting():
    data = request.get_json()
    Department = data[0]
    Team = data[1]
    Employee = data[2]

    def send_json(sendjson):
        sendjson = post("https://reqres.in/api/users", json=sendjson, headers={"Content-type": "application/json"})
        print(sendjson.text)
    send_json(Department)
    send_json(Team)
    send_json(Employee)

    return jsonify(Department, Team, Employee)


if __name__ == '__main__':
    app.run(debug=True)