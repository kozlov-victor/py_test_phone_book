import db_manager

def print_menu():
    print('1: create new record')
    print('2: read phone by name')
    print('3: update phone')
    print('4: delete record')
    print('5: exit')


def action_new_record():
    name = input('enter name>')
    phone = input('enter phone>')
    result = db_manager.new_record(name, phone)
    if result is True:
        print('new record has been created')


def action_read_phone_by_name():
    name = input('enter name>')
    phone = db_manager.read_phone_by_name(name)
    if phone is None:
        print('no such name')
    else:
        print(f'found: {phone}')


def action_update_phone():
    name = input('enter name>')
    phone = input('enter phone>')
    try:
        db_manager.update_phone(name, phone)
        print('phone has been updated')
    except ValueError as e:
        print(e)


def action_delete_record():
    name = input('enter name>')
    try:
        db_manager.delete_record(name)
        print('phone has been deleted')
    except ValueError as e:
        print(e)


def action_default() -> str:
    return 'wrong operation number'


def action_quit_app():
    print("done")
    quit(0)


actions = {
    '1': action_new_record,
    '2': action_read_phone_by_name,
    '3': action_update_phone,
    '4': action_delete_record,
    '5': action_quit_app
}