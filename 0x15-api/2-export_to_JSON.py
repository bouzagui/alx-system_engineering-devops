#!/usr/bin/python3
import json
import requests as req
import sys


def main():
    id_employee = int(sys.argv[1])

    url = "https://jsonplaceholder.typicode.com"
    url_user = req.get(f"{url}/users/{id_employee}").json()
    url_user_todos = req.get(f"{url}/users/{id_employee}/todos").json()

    filename = f"{id_employee}.json"
    username = url_user.get("username")
    new_list = []

    with open(filename, 'w', encoding="utf-8") as file:
        for item in url_user_todos:
            data = {
                "task": item.get("title"),
                "completed": item.get("completed"),
                "username": username,
            }
            new_list.append(data)
        output = {f"{id_employee}": new_list}
        json.dump(output, file)


if __name__ == "__main__":
    main()
