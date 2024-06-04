#!/usr/bin/python3

"""
Module that provides a function to export user tasks to a JSON file.
"""

import custom_methods
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} <user_id>\n")
        sys.exit(1)

    user_id = sys.argv[1]
    user = custom_methods.retrieve_username(user_id)
    if user is None:
        sys.stderr.write("Invalid user id.\n")
        sys.exit(1)

    todos = custom_methods.retrieve_todos(user_id)
    custom_methods.export_to_json(user_id=user_id, username=user, tasks=todos)
