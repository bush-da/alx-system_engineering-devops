#!/usr/bin/python3
"""Fetch dashboard id from datadog dashboards """
import sys
import requests
import json

def getId(api_key, app_key, dash_name):
    url = 'https://api.datadoghq.com/api/v1/dashboard'
    headers = {
        'Content-Type': 'application/json',
        'DD-API-KEY': api_key,
        'DD-APPLICATION-KEY': app_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        dashboards = response.json().get('dashboards', [])

        dashboard_id = None
        for dashboard in dashboards:
            if dashboard.get('title') == dash_name:
                dashboard_id = dashboard.get('id')
                break

        if dashboard_id:
            with open('2-setup_datalog', 'w') as file:
                file.write(dashboard_id + '\n')
            print(f'dashboard id written to 2-setup_datalog: {dashboard_id}')
        else:
            print('dashboard with specified name not found')
    else:
        print(f'Failed to fetch dashboards {response.status_code}')


if __name__ == '__main__':
    if (len(sys.argv) != 4):
        print(f"Usage: {sys.argv[0]} <API_KEY> <APPLICATION_KEY> <DASHBOARD_NAME>")
    else:
        getId(sys.argv[1], sys.argv[2], sys.argv[3])
