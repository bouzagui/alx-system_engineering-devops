#!/usr/bin/python3
"""models doc"""
import json
import requests as req


def main():
    id = 1
    data_dict = {}
    url = "https://jsonplaceholder.typicode.com"

    while True:
        user_response = req.get(f"{url}/users/{id}")
        if user_response.status_code != 200:
            break

        url_user = user_response.json()
        userName = url_user.get("username")

        todos_response = req.get(f"{url}/todos?userId={id}")
        todosData = todos_response.json()

        data_dict[id] = [
            {
                "username": userName,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todosData
        ]

        id += 1

    with open("todo_all_employees.json", "w") as f:
        json.dump(data_dict, f)


if __name__ == "__main__":
    main()
