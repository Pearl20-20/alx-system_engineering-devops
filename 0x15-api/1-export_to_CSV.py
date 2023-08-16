#!/usr/bin/python3
"""Accessing a rest Api for Todo list from eployee"""

import csv
import requests
import sys

if __name == '__main__':
    employeeId = sys.argv[1]
    baserUrl = "https://jsonplaceholder.typicode.com/user"
    url = baseUrl + "/" +  employeeId

    response = requests.get(url)
    username = response.json().get('username')
    tasks = response.json

    with open (f'{employeeId}.csv', 'w') as file:
        for task in tasks:
            file.write(f'"{employeeId}", "{username}", "{task.get('completed')}" "{task.get('title')}"\n')
~                                                                                                          
