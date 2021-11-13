import csv
from models.phonebookattribute import PhoneBookAttribute
from models.contact import Contact


def load():
    with open('db.csv', 'rt') as f:
        reader = csv.reader(f)
        rows = list(reader)
        db = {}
        for row in rows:
            if not row:
                continue
            name = row[0]
            mobile_num = PhoneBookAttribute('mobile', row[1])
            line_num = PhoneBookAttribute('line', row[2])
            email = PhoneBookAttribute('email', row[3])
            address = PhoneBookAttribute('address', row[4])
            contact = Contact(name,[mobile_num,line_num,email,address])
            db[name] = contact
        return db


def save(db):
    with open('db.csv', 'wt') as f:
        writer = csv.writer(f)
        for name, _ in db.items():
            contact = db[name]
            mobile_num = contact.get_val_by_attribute('mobile', '')
            line_num = contact.get_val_by_attribute('line', '')
            email = contact.get_val_by_attribute('email', '')
            address = contact.get_val_by_attribute('address', '')
            writer.writerow(
                (
                    contact.name,
                    mobile_num,
                    line_num,
                    address,
                    email
                )
            )
