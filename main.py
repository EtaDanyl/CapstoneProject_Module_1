from transaction_class import Transaction
from finance_tracker_class import FinanceTrackerData
import file_handler
import ui_handler
import docs_api_handler

MAIN_MENU = [
    "Add Transaction",
    "Edit Transaction",
    "All Transactions",
    "Statistics",
    "Generate a Report",
    "Exit",
    ]

EDITING_MENU = [
    "Amount",
    "Type",
    "Category",
    "Date",
    "Delete transaction",
    "Back",
    ]

FILTERING_SORTING_MENU = [
    "Amount",
    "Type",
    "Category",
    "Date",
    "Back",
]



def main():
    data = file_handler.load_data()
    tracker_data = FinanceTrackerData(data)
    tracker_data = run_tracker(tracker_data)

def run_tracker(tracker_data):
    ACTIONS = {
        0: add_transaction,
        1: edit_transaction,
        2: all_transactions,
        3: statistics,
        4: generate_report,
        5: exit_program
    }

    ui_handler.greet()

    action = 0
    while action != 5:
        action = ui_handler.menu(action, MAIN_MENU)
        ACTIONS[action](tracker_data)

    ui_handler.farewell()

def add_transaction(tracker_data):
    new_transaction_data = ui_handler.transaction_data()
    try:
        new_transaction = Transaction(**new_transaction_data)
    except:
        return
    else:
        tracker_data.transactions.append(new_transaction)

def edit_transaction(tracker_data):
    global EDITING_MENU
    starting_pointer_position = 0
    position = ui_handler.menu(starting_pointer_position, tracker_data.transactions)
    transaction_to_edit = tracker_data.transactions[position]
    edited_transaction = ui_handler.edit_transaction(transaction_to_edit, EDITING_MENU)
    if edited_transaction is None:
        tracker_data.transactions.pop(position)
    else:
        tracker_data.transactions[position] = edited_transaction

    print(f"Old: {transaction_to_edit}")
    print(f"New: {edited_transaction}")

    input()


def all_transactions(tracker_data):
    ui_handler.print_all_transactions(tracker_data.transactions, FILTERING_SORTING_MENU)

def statistics(tracker_data):
    ui_handler.print_statistics(tracker_data)

def generate_report(tracker_data):
    docs_api_handler.call_api(tracker_data.transactions)

def exit_program(tracker_data):
    file_handler.save_data(tracker_data.transactions)

if __name__ == "__main__":
    main()