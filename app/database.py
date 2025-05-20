import os
import json


base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "patients.json")

def load_data():
    try:
        with open(file_path, "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return []

def save_data(data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

        