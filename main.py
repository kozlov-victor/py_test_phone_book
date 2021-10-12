import pickle
import json

running = True
db = {}

"""
db functions
"""

PICKLE_SERIALIZER_TYPE = 'pickle'
JSON_SERIALIZER_TYPE = 'json'


def load_db_json():
    global db
    with open('db.json', 'rt') as f:
        db = json.load(f)
        print('json db has been loaded')


def save_db_json():
    global db
    with open('db.json', 'wt') as f:
        json.dump(db, f)


def load_db_pickle():
    global db
    with open('db.pickle', 'rb') as f:
        db = pickle.load(f)
        print('pickle db has been loaded')


def save_db_pickle():
    global db
    with open('db.pickle', 'wb') as f:
        pickle.dump(db, f)



"""
decorator functions
"""


def check_name_exists(message):
    def decorator(f):
        def wrapper(*args):
            if args[0] in db:
                raise ValueError(message)
            else:
                return f(*args)

        return wrapper

    return decorator


def check_name_does_not_exist(message):
    def decorator(f):
        def wrapper(*args):
            if args[0] not in db:
                raise ValueError(message)
            else:
                return f(*args)

        return wrapper

    return decorator


"""
business logic functions
"""


@check_name_exists('name already exists')
def new_record(name: str, phone: str):
    db[name] = phone
    save_db()


def read_phone_by_name(name: str) -> str:
    return db.get(name, None)


@check_name_does_not_exist('can not update: no such name')
def update_phone(name: str, phone: str):
    db[name] = phone
    save_db()


@check_name_does_not_exist('can not delete: no such name')
def delete_record(name: str):
    del db[name]
    save_db()


"""
Controller functions
"""


def print_menu():
    print('1: create new record')
    print('2: read phone by name')
    print('3: update phone')
    print('4: delete record')
    print('5: exit')


def action_new_record():
    name = input('enter name>')
    phone = input('enter phone>')
    result = new_record(name, phone)
    if result is True:
        print('new record has been created')


def action_read_phone_by_name():
    name = input('enter name>')
    phone = read_phone_by_name(name)
    if phone is None:
        print('no such name')
    else:
        print(f'found: {phone}')


def action_update_phone():
    name = input('enter name>')
    phone = input('enter phone>')
    try:
        update_phone(name, phone)
        print('phone has been updated')
    except ValueError as e:
        print(e)


def action_delete_record():
    name = input('enter name>')
    try:
        delete_record(name)
        print('phone has been deleted')
    except ValueError as e:
        print(e)


def action_default() -> str:
    return 'wrong operation number'


def action_quit_app() -> str:
    global running
    running = False
    return 'bye'


actions = {
    '1': action_new_record,
    '2': action_read_phone_by_name,
    '3': action_update_phone,
    '4': action_delete_record,
    '5': action_quit_app
}

"""
main
"""

try:
    with open('config.conf', 'rt') as f:
        serializer_type = f.readline()
        if serializer_type == PICKLE_SERIALIZER_TYPE:
            (load_db, save_db) = load_db_pickle, save_db_pickle
        elif serializer_type == JSON_SERIALIZER_TYPE:
            (load_db, save_db) = load_db_json, save_db_json
        else:
            raise ValueError('wrong serializer type')
        load_db()
        print('data base has been loaded')
except Exception as e:
    print('data base loading error: ', e)

while running:
    print_menu()
    action = input('select item from menu>')
    actions.get(action, action_default)()
