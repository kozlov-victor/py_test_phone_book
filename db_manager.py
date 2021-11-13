import config_reader
from models.contact import Contact
from models.phonebookattribute import PhoneBookAttribute


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
                return f(name,*args)

        return wrapper

    return decorator


def check_name_does_not_exist(message):
    def decorator(f):
        def wrapper(name, *args):
            if name not in _db:
                raise ValueError(message)
            else:
                return f(name,*args)

        return wrapper

    return decorator


@check_name_exists('name already exists')
def new_record(name: str, attr: PhoneBookAttribute):
    contact = Contact(name, [attr])
    _db[name] = contact
    _save(_db)


def read_contact_by_name(name: str) -> Contact:
    if name not in _db:
        raise ValueError('no such name')
    return _db.get(name)


@check_name_does_not_exist('can not update: no such name')
def update_attribute(name: str, attribute: PhoneBookAttribute):
    contact = _db[name]
    attribute_to_find = [x for x in contact.attributes if x.type == attribute.type]
    if not attribute_to_find:
        contact.attributes.append(attribute)
    else:
        attribute_to_find[0].value = attribute.value
    _save(_db)


@check_name_does_not_exist('can not delete: no such name')
def delete_record(name: str):
    del _db[name]
    _save(_db)
