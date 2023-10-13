#!/usr/bin/python3
"""
Write a script that hits a REST api that has data on employees and tasks
and filters the data based on an argument passed to the script.
The argument is the employee ID, and the output should display the employee
name and the tasks the employee completed.
"""

import json
import sys
from urllib import request


if __name__ == '__main__':
    url1 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        sys.argv[1])
    url2 = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])

    resp1 = request.urlopen(url1)
    resp2 = request.urlopen(url2)

    user = json.loads(resp2.read())
    todos = json.loads(resp1.read())

    done = (int(todo['completed']) for todo in todos)
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), sum(done), len(todos)))
    for todo in todos:
        if todo['completed']:
            print("\t {}".format(todo.get("title")))
