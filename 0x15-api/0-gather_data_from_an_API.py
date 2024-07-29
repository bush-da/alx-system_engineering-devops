#!/usr/bin/env python3
"""
The module that defines get employee todo list using restapi
"""
import requests
import sys


def get_emp_todo_list(emp_id):
    """ base URL to get todo list """
    base_url = 'https://jsonplaceholder.typicode.com'

    """ getting user URL From base url"""
    user_url = f"{base_url}/users/{emp_id}"

    response = requests.get(user_url)
    """ check if the employee exists """
    if response.status_code != 200:
        print(f"User with ID {emp_id} not found")
        return

    emp = response.json()
    """ get employee name """
    emp_name = emp['name']

    todos_url = f'{base_url}/todos?userId={emp_id}'
    response = requests.get(todos_url)
    todos = response.json()

    """ list all done tasks of the employee """
    done_tasks = [todo for todo in todos if todo['completed']]
    tot_tasks = len(todos)
    DoneTasks = len(done_tasks)

    print(f"Employee {emp_name} is done with tasks({DoneTasks}/{tot_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python3 0-gather_data_from_an_API.py emp_id")
    else:
        try:
            emp_id = int(sys.argv[1])
            get_emp_todo_list(emp_id)
        except ValueError:
            print("The employee ID must be integer")
