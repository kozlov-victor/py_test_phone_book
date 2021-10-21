import json

from models.contact import Contact


def load():
    with open('db.json', 'rt') as f:
        raw_map = json.load(f)
        db = {}
        for key,val in raw_map.items():
            db[key] = Contact().from_dict({"phone":val})
        print('json db has been loaded')
        return db


def save(db: dict):
    db_to_save = {}
    with open('db.json', 'wt') as f:
        for key,contact in db.items():
            db_to_save[key] = contact.to_dict()
        json.dump(db_to_save, f)
