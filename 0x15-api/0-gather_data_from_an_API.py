#!/usr/bin/python3

"""
Script that takes an employee ID and returns the information about his/her
TODO list progress. Specifically, the ones they have completed.
"""

import custom_methods
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} <user_id>\n")
        sys.exit(1)

    user = custom_methods.retrieve_name(sys.argv[1])
    if user is None:
        sys.stderr.write("Invalid user id.\n")
        sys.exit(1)

    todos = custom_methods.retrieve_todos(sys.argv[1])
    completed_tasks = custom_methods.retrieve_completed_tasks(todos)
    custom_methods.print_completed_tasks(user, len(todos), completed_tasks)
