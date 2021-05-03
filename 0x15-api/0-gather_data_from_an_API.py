#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


import requests
from sys import argv


if __name__ == "__main__":
    employee_ID = argv[1]

    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                            format(employee_ID), verify=False).json()

    todo_list = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(employee_ID), verify=False).json()
    completed = []
    for task in todo_list:
        if task.get('completed') is True:
            completed.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(employee.get('name'), len(completed), len(todo_list)))
    print("\n".join("\t {}".format(task) for task in completed))
