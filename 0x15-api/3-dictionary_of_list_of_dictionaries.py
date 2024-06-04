#!/usr/bin/python3

"""
Module that provides a function to export all tasks to a JSON file.
"""

import custom_methods


if __name__ == "__main__":
    # get user info and todos once so we can minimize the number of requests.
    # this helps to achieve more speed since everything will be done locally
    # after the data has been retrieved.
    users = custom_methods.retrieve_users()
    todos = custom_methods.retrieve_todos()
    custom_methods.export_all_to_json(users=users, tasks=todos)
