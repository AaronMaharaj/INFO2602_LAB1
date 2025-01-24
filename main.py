from flask import Flask, request, jsonify
import json

from flask.typing import BeforeFirstRequestCallable

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response


@app.route('/students')
def get_students():
    result = []
    pref = request.args.get('pref')
    if pref:
        for student in data:
            if student['pref'] == pref:
                result.append(student)
        return jsonify(result)
    return jsonify(data)


@app.route('/students/<id>')
def get_student(id):
    error_message = {
        "message": "Student not found.",
        "error_code": 404,
        "details": "Check the student ID and try again."
    }
    for student in data:
        if student['id'] == id:
            return jsonify(student)
    return jsonify(error_message), 404


@app.route('/stats')
def get_stats():
    statsDict = {
        "Computer Science (Major)": 0,
        "Computer Science (Special)": 0,
        "Information Technology (Major)": 0,
        "Information Technology (Special)": 0,
        "Vegetable": 0,
        "Chicken": 0,
        "Fish": 0
    }
    for student in data:
        pref = student.get("pref")
        programme = student.get("programme")
        if pref in statsDict:
            statsDict[pref] += 1
        if programme in statsDict:
            statsDict[programme] += 1
    print(statsDict)
    return jsonify(statsDict)


@app.route('/add/<a>/<b>')
def add(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return jsonify(c)


@app.route('/subtract/<a>/<b>')
def subtract(a, b):
    a = int(a)
    b = int(b)
    c = a - b
    return jsonify(c)


@app.route('/multiply/<a>/<b>')
def multiply(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return jsonify(c)


@app.route('/divide/<a>/<b>')
def divide(a, b):
    a = int(a)
    b = int(b)
    if b == 0:
        error_message = {
            "message": "Division by 0 is invalid.",
            "error_code": 400,
            "details": "Try division with nonzero numbers instead."
        }
        return jsonify(error_message), 400
    c = a / b
    return jsonify(c)


app.run(host='0.0.0.0', port=8080, debug=True)
