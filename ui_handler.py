import keyboard
import uuid
from datetime import datetime

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
    print("\nUse ↑ ↓ to navigate. Enter to select.\n")

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
    if temp_amount is None:
        return None
    temp_type = get_type()
    if temp_type is None:
        return None
    temp_category = get_category()
    if temp_category is None:
        return None
    temp_date = get_date()
    if temp_date is None:
        return None
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
        user_input = input("Enter the amount. Type 'Cancel' to go back: ").strip().lower()
        if user_input == "cancel":
            return None
        try:
            amount = float(user_input)
        except:
            print("Wrong input. Enter a number.")
            continue
        else:
            return amount

def get_type():
    while True:
        user_input = input("Choose between two types: 'Income' or 'Expense'. Type 'Cancel' to go back: ").strip().lower()
        
        match user_input:
            case "cancel":
                return None
            case "income":
                return user_input
            case "expense":
                return user_input
            case _:
                print("Wrong input. Try again.")


def get_category():
    user_input = input("Choose a category. Type 'Cancel' to go back: ").strip().lower()
    if user_input == "cancel":
        return None
    else:
        return user_input.capitalize()

def get_date():
    while True:
        user_input = input("Enter the date in YYYY-MM-DD format. Type 'Cancel' to go back: ").strip().lower()
        if user_input == "cancel":
            return None
        try:
            parsed_date = datetime.strptime(user_input, "%Y-%m-%d").date()
        except:
            print("Wrong input. Try again.")
            continue
        else:
            return parsed_date

def get_transaction_id():
    return str(uuid.uuid4())

def print_all_transactions(transactions):
    if len(transactions) > 0:
        [print(tr) for tr in transactions]
    else:
        print("No transactions.")

    input("\nPress 'Enter' to go back.")
    return

def print_statistics(tracker_data):
    print(tracker_data)

    input("Press 'Enter' to go back.")
    return