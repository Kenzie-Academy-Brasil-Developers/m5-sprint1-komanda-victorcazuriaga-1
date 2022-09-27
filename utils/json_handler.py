from genericpath import exists
import json


def generate_id(filepath):
    try:
        data = read_json(filepath)[-1]["id"] + 1
        return int(data)
    except:
        return 1


def write_json(filepath, data):
    data["id"] = generate_id(filepath)
    old_data = read_json(filepath)
    new_data = [*old_data, data]
    print(new_data)
    with open(filepath, 'w') as file:
        json.dump(new_data, file, ensure_ascii=False, indent=2)
    return data


def read_json(filepath: str):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return []
