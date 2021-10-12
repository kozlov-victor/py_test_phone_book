import config_reader

_db = {}
_load, _save = config_reader.resolve_serializers()


def load_db():
    global _db
    _db = _load()


def check_name_exists(message):
    def decorator(f):
        def wrapper(*args):
            if args[0] in _db:
                raise ValueError(message)
            else:
                return f(*args)

        return wrapper

    return decorator


def check_name_does_not_exist(message):
    def decorator(f):
        def wrapper(*args):
            if args[0] not in _db:
                raise ValueError(message)
            else:
                return f(*args)

        return wrapper

    return decorator


@check_name_exists('name already exists')
def new_record(name: str, phone: str):
    _db[name] = phone
    _save(_db)


def read_phone_by_name(name: str) -> str:
    return _db.get(name, None)


@check_name_does_not_exist('can not update: no such name')
def update_phone(name: str, phone: str):
    _db[name] = phone
    _save()


@check_name_does_not_exist('can not delete: no such name')
def delete_record(name: str):
    del _db[name]
    _save()
