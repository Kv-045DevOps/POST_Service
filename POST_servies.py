from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/posting', methods=['POST'])
def posting():
    data = request.get_json()
    Department = data[0]
    Team = data[1]
    Employee = data[2]
    return jsonify(Department, Team, Employee)


if __name__ == '__main__':
    app.run(debug=True)
