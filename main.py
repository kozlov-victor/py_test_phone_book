import db_manager
import phone_book_controller

running = True


def print_menu():
    print(
        """
        1: create new record
        2: read contact by name
        3: update contact attribute
        4: delete record
        5: exit
        """
    )


def action_default() -> str:
    return 'wrong operation number'


def action_quit_app():
    print("done")
    global running
    running = False


actions = {
    '1': phone_book_controller.action_new_record,
    '2': phone_book_controller.action_read_contact_by_name,
    '3': phone_book_controller.action_update_contact_attribute,
    '4': phone_book_controller.action_delete_record,
    '5': action_quit_app
}

try:
    db_manager.load_db()
except Exception as e:
    print('data base loading error: ', e)

while running:
    print_menu()
    action = input('select item from menu>')
    try:
        actions.get(action, action_default)()
    except ValueError as e:
        print(e)
