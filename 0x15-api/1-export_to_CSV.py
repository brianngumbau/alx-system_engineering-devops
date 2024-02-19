#!/usr/bin/python3

"""
exports data in the CSV format
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for k in data2:
        if k['id'] == int(argv[1]):
            employee = k['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        write = csv.writer(file, quoting=csv.QUOTE_ALL)

        for k in data:

            row = []
            if k['userId'] == int(argv[1]):
                row.append(k['userId'])
                row.append(employee)
                row.append(k['completed'])
                row.append(k['title'])

                write.writerow(row)
