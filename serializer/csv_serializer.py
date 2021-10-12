import csv

"""
warning! not tested at all!
"""


def load():
    with open('db.csv', 'rt') as f:
        db = csv.reader(f)
        print('csv db has been loaded')
        return db


def save(db):
    with open('db.csv', 'rt') as f:
        writer = csv.writer(f)
        writer.writerows(db)
