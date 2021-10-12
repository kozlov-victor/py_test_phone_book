import db_manager
import phone_book_controller

running = True


try:
    db_manager.load_db()
except Exception as e:
    print('data base loading error: ', e)

while running:
    phone_book_controller.print_menu()
    action = input('select item from menu>')
    phone_book_controller.actions.get(action, phone_book_controller.action_default)()
