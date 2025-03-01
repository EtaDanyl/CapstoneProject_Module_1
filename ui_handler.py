import keyboard
import uuid
from datetime import datetime

def print_menu(pointer_position, options):
    for i, option in enumerate(options):
        prefix = "> " if i == pointer_position else "  "
        print(prefix, option)
    print("\nUse ↑ ↓ to navigate. Enter to select.\n")

def menu(pointer_position, options):
    print_menu(pointer_position, options)
    while True:
        key_event = keyboard.read_event(suppress=True)

        if key_event.event_type == keyboard.KEY_UP:
            if key_event.name == "up":
                pointer_position = (pointer_position - 1) % len(options)
            elif key_event.name == "down":
                pointer_position = (pointer_position + 1) % len(options)
            print("\033c", end="")
            print_menu(pointer_position, options)
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
    if temp_type == "expense":
        temp_amount *= -1
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

def print_all_transactions(transactions, filtering_sorting_menu):
    temp_transactions = transactions
    while True:
        print("\033c", end="")
        if len(temp_transactions) > 0:
            [print(tr) for tr in temp_transactions]
        else:
            print("No transactions.")

        user_input = input("\nChoose by inputing: 'Sort', 'Filter', 'Refresh', 'Back': ").strip().lower()
        match user_input:
            case "sort": 
                temp_transactions = sort_transactions(temp_transactions, filtering_sorting_menu)
            case "filter": 
                temp_transactions = filter_transactions(temp_transactions, filtering_sorting_menu)
            case "refresh": 
                temp_transactions = transactions
            case "back":
                break
            case _:
                print("Wrong input. Try again.")

def sort_transactions(temp_transactions, filtering_sorting_menu):
    sort_keys = {0: "amount", 1: "transaction_type", 2: "category", 3: "date"}

    action = 0
    action = menu(action, filtering_sorting_menu)

    if action != 4:
        temp_transactions = quick_sort(temp_transactions, sort_keys[action])

    return temp_transactions

def quick_sort(transactions, key):
    if len(transactions) <= 1:
        return transactions
    pivot = transactions[len(transactions) // 2]
    left = [t for t in transactions if getattr(t, key) < getattr(pivot, key)]
    middle = [t for t in transactions if getattr(t, key) == getattr(pivot, key)]
    right = [t for t in transactions if getattr(t, key) > getattr(pivot, key)]
    return quick_sort(left, key) + middle + quick_sort(right, key)

def filter_transactions(temp_transactions, filtering_sorting_menu):
    filter_options = {0: filter_by_amount, 1: filter_by_type, 2: filter_by_category, 3: filter_by_date}

    action = 0
    action = menu(action, filtering_sorting_menu)

    if action != 4:
        temp_transactions = filter_options[action](temp_transactions)

    return temp_transactions

def filter_by_amount(temp_transactions):
    print("Define a minimum amount:")
    min = get_amount()
    if min is None :
        return temp_transactions
    
    print("Define a maximum amount:")
    max = get_amount()
    if  max is None:
        return temp_transactions

    if min > max:
        temp_min = min
        min = max
        max = temp_min

    return [t for t in temp_transactions if min <= t.amount <= max]

         
def filter_by_type(temp_transactions):
    income_or_expense = get_type()
    if income_or_expense is None :
        return temp_transactions
    
    return [t for t in temp_transactions if t.transaction_type == income_or_expense]

def filter_by_category(temp_transactions):
    category = get_category()
    if category is None :
        return temp_transactions
    
    return [t for t in temp_transactions if t.category == category]

def filter_by_date(temp_transactions):
    print("From:")
    start_date = get_date()
    if start_date is None :
        return temp_transactions
    
    print("Until:")
    end_date = get_date()
    if  end_date is None:
        return temp_transactions

    if start_date > end_date:
        temp_start_date = start_date
        start_date = end_date
        end_date = temp_start_date

    return [t for t in temp_transactions if start_date <= t.date <= end_date]
    
def print_statistics(tracker_data):
    print("\033c", end="")
    print(tracker_data)

    input("Press 'Enter' to go back.")
    return

def edit_transaction(transaction_to_edit, editing_menu):
    action = 0
    while action != 5:
        action = menu(action, editing_menu)

        match action:
            case 0: 
                temp_amount = get_amount()
                if temp_amount is None:
                    continue
                else:
                    transaction_to_edit.amount = temp_amount
            case 1: 
                temp_type = get_type()
                if temp_type is None:
                    continue
                else:
                    transaction_to_edit.transaction_type = temp_type
            case 2: 
                temp_category = get_category()
                if temp_category is None:
                    continue
                else:
                    transaction_to_edit.category = temp_category
            case 3: 
                temp_date = get_date()
                if temp_date is None:
                    continue
                else:
                    transaction_to_edit.date = temp_date
            case 4: 
                transaction_to_edit = None
                break

    input("Changes saved. Press 'Enter' to continue.")
    return transaction_to_edit