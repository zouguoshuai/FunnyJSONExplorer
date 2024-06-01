import json


def JsonLoader(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data
