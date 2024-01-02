#!/usr/bin/python3
"""returns information using REST API about a given
    employee ID TODO list progress.
"""
import requests
from sys import argv


def get_todo_list(employee_id):
    """fetch TODO list for employee ID"""
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    todos = response.json()

    # get employee name
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_response = requests.get(user_url)
    EMPLOYEE_NAME = user_response.json()['name']

    # calc TODO progress
    TOTAL_NUM_OF_TASKS = len(todos)
    done_tasks = [todo for todo in todos if todo['completed']]
    NUM_OF_DONE_TASKS = len(done_tasks)

    # display progress info
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUM_OF_DONE_TASKS,
                                                          TOTAL_NUM_OF_TASKS))
    # completed task
    for task in done_tasks:
        print("\t {}".format(task['title']))


if __name__ == "__main__":
    try:
        employee_id = int(argv[1])
    except ValueError:
        exit()

    get_todo_list(employee_id)
