from flask import Flask, request
import json
from task_runner import TaskRunner

app = Flask(__name__)

@app.route('/ping')
def hello_world():
    return 'pong'

@app.route('/submit-tasks', methods=['POST'])
def submit_tasks():
    tasks = request.json['tasks']
    TaskRunner().submit_tasks(tasks)
    return {'msg':'success'}


if __name__ == '__main__':
    app.run(debug=True)