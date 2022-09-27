from genericpath import exists
import json


def generate_id():
    try:
        data = read_json('menu.json')[-1]["id"] + 1
        return int(data)
    except:
        return 1


def write_json(filepath, data):
    data["id"] = generate_id()
    old_data = read_json('menu.json')
    new_data = [*old_data, data]
    with open(filepath, 'w') as file:
        json.dump(new_data, file, ensure_ascii=False)
        return data


def read_json(filepath: str):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return []
