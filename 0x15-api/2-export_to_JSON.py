#!/usr/bin/python3
import json
import requests as req
import sys


def main():
    ID_Employee = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(ID_Employee)
    url_to_do = "https://jsonplaceholder.typicode.com/users/{}/todos/".format(
        ID_Employee)
    response = req.get(url).json()
    username = response.get('username')
    response_to_dos = req.get(url_to_do).json()
    new_list = []
    my_dict = dict()

    with open(f'{ID_Employee}.json', 'w', encoding="utf-8") as file:
        for item in response_to_dos:
            new_one = {
                "task": item['title'],
                "completed": item['completed'],
                "username": username}
            new_list.append(new_one)
        my_dict['{}'.format(ID_Employee)] = new_list
        my_content = json.dumps(my_dict)
        file.write(my_content + "\n")


if __name__ == "__main__":
    main()
