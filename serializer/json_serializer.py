import json


def load():
    with open('db.json', 'rt') as f:
        db = json.load(f)
        print('json db has been loaded')
        return db


def save(db):
    with open('db.json', 'wt') as f:
        json.dump(db, f)
