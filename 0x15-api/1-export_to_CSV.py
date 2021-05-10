#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId)).json()

    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(userId)).json()
    with open("{}.csv".format(userId), 'w') as acsvfile:
        csvwriter = csv.writer(acsvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            csvwriter.writerow([userId, name.get('username'),
                                task.get('completed'), task.get('title')])
