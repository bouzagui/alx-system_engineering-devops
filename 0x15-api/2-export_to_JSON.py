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
    my_dict = dict()

    with open(filename, 'w', encoding="utf-8") as file:
        for item in url_user_todos:
            new_one = {
                "task": item['title'],
                "completed": item['completed'],
                "username": username}
            new_list.append(new_one)
        my_dict['{}'.format(id_employee)] = new_list
        my_content = json.dumps(my_dict)
        file.write(my_content + "\n")


if __name__ == "__main__":
    main()
