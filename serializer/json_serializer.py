import json
from models.phonebookattribute import PhoneBookAttribute

from models.contact import Contact


def load():
    with open('db.json', 'rt') as f:
        raw_map = json.load(f)
        db = {}
        for key,val in raw_map.items():
            attributes = [PhoneBookAttribute(a["type"], a["value"]) for a in val["attributes"]]
            db[key] = Contact(key,attributes)
        print('json db has been loaded')
        print(db)
        return db


def save(db: dict):
    db_to_save = {}
    with open('db.json', 'wt') as f:
        for key,contact in db.items():
            db_to_save[key] = contact.to_dict()
        json.dump(db_to_save, f)
