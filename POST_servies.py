from flask import Flask
import json

"""Parsing!!!"""
#-------------------------------------------------------------
pull_json = json.load(open('all_persons.json'))
Department = pull_json[0]
Team = pull_json[1]
Employee = pull_json[2]
print(Department, Team, Employee)

with open('department.json', 'w') as file:
    json.dump(Department, file, indent=2, ensure_ascii=False)

with open('team.json', 'w') as file:
    json.dump(Team, file, indent=2, ensure_ascii=False)

with open('employee.json', 'w') as file:
    json.dump(Employee, file, indent=2, ensure_ascii=False)
#-------------------------------------------------------------


# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return "<h1> Test </h1>"
#
# if __name__ == '__main__':
#     app.run(debug=True)