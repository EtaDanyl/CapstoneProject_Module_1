import keyboard

options = [
    "Add Transaction",
    "Edit Transaction",
    "All Transactions",
    "Statistics",
    "Generate a Report",
    "Exit",
    ]

def print_menu(pointer_position):
    for i, option in enumerate(options):
        prefix = "> " if i == pointer_position else "  "
        print(prefix + option)
    print("\nUse ↑ ↓ to navigate, Enter to select.")

def menu(pointer_position):
    print_menu(pointer_position)
    while True:
        key_event = keyboard.read_event(suppress=True)

        if key_event.event_type == keyboard.KEY_UP:
            if key_event.name == "up":
                pointer_position = (pointer_position - 1) % len(options)
            elif key_event.name == "down":
                pointer_position = (pointer_position + 1) % len(options)
            print("\033c", end="")
            print_menu(pointer_position)
        elif key_event.event_type == keyboard.KEY_DOWN:
            if key_event.name == "enter":
                return pointer_position


def greet():
    print("Welcome! I am your Personal Finance Tracker & Budget Assistant")

def farewell():
    print("I'll see you next time!")

def transaction_data():
    print("Creating a new transaction")
    temp_amount = get_amount()
    temp_type = get_type()
    temp_category = get_category()
    temp_date = get_date()
    temp_id = get_transaction_id()

    temp_transaction_data = {
        "amount": temp_amount,
        "transaction_type": temp_type,
        "category": temp_category,
        "date": temp_date,
        "transaction_id": temp_id,
    }

    return temp_transaction_data

def get_amount():
    while True:
        amount = float(input("Enter the amount: "))

def get_type():
    pass

def get_category():
    pass

def get_date():
    pass

def get_transaction_id():
    pass

