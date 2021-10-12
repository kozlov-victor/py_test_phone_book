import pickle


def load():
    with open('db.pickle', 'rb') as f:
        db = pickle.load(f)
        print('pickle db has been loaded')
        return db


def save(db):
    with open('db.pickle', 'wb') as f:
        pickle.dump(db, f)
