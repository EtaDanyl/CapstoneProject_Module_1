from transaction_class import Transaction
from finance_tracker_class import FinanceTrackerData
import file_handler
import ui_handler
import docs_api_handler
from menus import Menu

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
        action = ui_handler.menu(action, Menu.main)
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
    data = ui_handler.choose_transaction_to_edit(tracker_data.transactions, Menu.editing)
    edited_transaction = data[0]
    position = data[1]
    if position is None:
        return
    elif edited_transaction is None:
        tracker_data.transactions.pop(position)
    else:
        tracker_data.transactions[position] = edited_transaction

def all_transactions(tracker_data):
    ui_handler.print_all_transactions(tracker_data.transactions, Menu.filtering_sorting)

def statistics(tracker_data):
    ui_handler.print_statistics(tracker_data)

def generate_report(tracker_data):
    docs_api_handler.call_api(tracker_data.transactions)

def exit_program(tracker_data):
    file_handler.save_data(tracker_data.transactions)

if __name__ == "__main__":
    main()