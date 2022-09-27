from genericpath import exists
import json


def generate_id():
    try:
        data = read_json('menu.json')[-1]["id"] + 1
        yield data
    except:
        yield 1


def write_json(filepath, data):
    data["id"] = next(generate_id())
    old_data = read_json('menu.json')
    new_data = [*old_data, data]
    with open(filepath, 'w') as file:
        json.dump(new_data, file, ensure_ascii=False)


def read_json(filepath: str):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        with open(filepath, 'w') as file:
            data = {}
            json.dump([], file, ensure_ascii=False)
