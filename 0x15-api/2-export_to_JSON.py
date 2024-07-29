#!/usr/bin/python3
"""
 get employee tasks using api and export it into CSV file
"""
import json
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
    emp_name = emp.get("username")

    todos_url = f'{base_url}/todos?userId={emp_id}'
    response = requests.get(todos_url)
    todos = response.json()

    """ preparing the data for json """
    json_data = {emp_id: []}
    for todo in todos:
        json_data[emp_id].append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": emp_name
            })

    """ writing the data to a json file """
    json_filename = f'{emp_id}.json'
    with open(json_filename, 'w', newline='') as jsonfile:
        writer = json.dump(json_data, jsonfile)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python3 0-gather_data_from_an_API.py emp_id")
    else:
        try:
            emp_id = int(sys.argv[1])
            get_emp_todo_list(emp_id)
        except ValueError:
            print("The employee ID must be integer")
