import db_manager


def action_new_record():
    name = input('enter name>')
    phone = input('enter phone>')
    db_manager.new_record(name, phone)
    print('new record has been created')


def action_read_phone_by_name():
    name = input('enter name>')
    contact = db_manager.read_phone_by_name(name)
    print(f'found: {contact.phone}')


def action_update_phone():
    name = input('enter name>')
    phone = input('enter phone>')
    db_manager.update_phone(name, phone)
    print('phone has been updated')


def action_delete_record():
    name = input('enter name>')
    try:
        db_manager.delete_record(name)
        print('phone has been deleted')
    except ValueError as e:
        print(e)
