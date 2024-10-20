import json

users = [
    {"username": "Checking2@percepti.co", "password": "Checking2@percepti.c"},
    {"username": "Checking@percepti.co", "password": "Checking@percepti.c1"}
]

filename = "../.venv/users.json"

with open(filename, 'w') as json_file:
    json.dump(users, json_file, indent=4)
