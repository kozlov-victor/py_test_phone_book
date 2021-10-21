import config_reader
from models.contact import Contact

"""
    _db - dictionary with key:string and value:Contact
"""
_db = {}
_serializer = config_reader.resolve_serializer_module()
_load, _save = _serializer.load, _serializer.save


def load_db():
    global _db
    _db = _load()


def check_name_exists(message):
    def decorator(f):
        def wrapper(name, *args):
            if name in _db:
                raise ValueError(message)
            else:
                return f(*args)

        return wrapper

    return decorator


def check_name_does_not_exist(message):
    def decorator(f):
        def wrapper(name, *args):
            if name not in _db:
                raise ValueError(message)
            else:
                return f(*args)

        return wrapper

    return decorator


@check_name_exists('name already exists')
def new_record(name: str, phone: str):
    contact = Contact()
    contact.from_dict({"phone": phone})
    _db[name] = contact
    _save(_db)


def read_phone_by_name(name: str) -> Contact:
    if name not in _db:
        raise ValueError('no such name')
    return _db.get(name)


@check_name_does_not_exist('can not update: no such name')
def update_phone(name: str, phone: str):
    _db[name].phone = phone
    _save()


@check_name_does_not_exist('can not delete: no such name')
def delete_record(name: str):
    del _db[name]
    _save()
