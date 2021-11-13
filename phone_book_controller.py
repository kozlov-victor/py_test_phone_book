import db_manager
from models.phonebookattribute import PhoneBookAttribute


def print_attribute_menu():
    print(
        """
        1: mobile phone number
        2: line phone number
        3: address
        4: email
        """
    )


def get_attribute_type(option: str) -> str:
    if option == '1':
        return 'mobile'
    elif option == '2':
        return 'line'
    elif option == '3':
        return 'address'
    elif option == '4':
        return 'email'
    raise ValueError(f"option ${option} is not implemented")


def action_new_record():
    name = input('enter name>')
    print("Choose attribute to create:")
    print_attribute_menu()
    attribute_type = get_attribute_type(input())
    attribute_value = input('enter attribute value>')
    attribute = PhoneBookAttribute(attribute_type, attribute_value)
    db_manager.new_record(name, attribute)
    print('new record has been created')


def action_read_contact_by_name():
    name = input('enter name>')
    contact = db_manager.read_contact_by_name(name)
    print(f'---------contact card: {contact.name}--------')
    for a in contact.attributes:
        print(f'{a.type}: {a.value}')


def action_update_contact_attribute():
    name = input('enter name>')
    print("Choose attribute to update:")
    print_attribute_menu()
    attribute_type = get_attribute_type(input())
    attribute_value = input('enter attribute value>')
    attribute = PhoneBookAttribute(attribute_type, attribute_value)
    db_manager.update_attribute(name, attribute)
    print('the contact has been updated')


def action_delete_record():
    name = input('enter name>')
    try:
        db_manager.delete_record(name)
        print(f'the record with name "${name}" has been deleted')
    except ValueError as e:
        print(e)
