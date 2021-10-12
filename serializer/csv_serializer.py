import csv

"""
still doesn't work(
"""


def load():
    with open('db.csv', 'rt') as infile:
        reader = csv.reader(infile)
        db = {}
        for rows in reader:
            k = rows[0]
            v = rows[1]
            db[k] = v
        print("loaded", db)
        return db


def save(db):
    with open('db.csv', 'wt') as f:
        writer = csv.writer(f)
        for key in db.keys():
            print('saving',key,db[key])
            writer.writerow([key,db[key]])
