#!/usr/bin/python3
"""
 get all employee tasks using api and export it into JSON file
"""
import json
import requests
import sys

if __name__ == '__main__':

    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    """ request resource and format it into json """
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    todo_all_employee = dict()

    """ create format for all employee to write into json file """
    for user in users:
        user_id = user['id']
        user_name = user['username']
        user_tasks = [task for task in todos if task['userId'] == user_id]

        todo_all_employee[user_id] = [
            {
                'username': user_name,
                'task': task['title'],
                'completed': task['completed']
            } for task in user_tasks
        ]

        filename = "todo_all_employees.json"
        with open(filename, 'w') as filejson:
            json.dump(todo_all_employee, filejson)
