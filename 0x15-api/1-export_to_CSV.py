#!/usr/bin/python3
"""models doc"""
import requests as req
import sys


def main():
    id_employee = int(sys.argv[1])

    url = "https://jsonplaceholder.typicode.com"
    url_user = req.get(f"{url}/users/{id_employee}").json()
    url_user_todos = req.get(f"{url}/users/{id_employee}/todos").json()

    username = url_user.get("username")
    filename = f"{id_employee}.csv"
    with open(filename, 'w', encoding="utf-8") as file:
        for todos in url_user_todos:
            data = f'"{id_employee}","{username}","{todos.get("completed")}",'
            data2 = f'"{todos.get("title")}"\n'
            file.write(data+data2)


if __name__ == "__main__":
    main()
