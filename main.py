from transaction_class import Transaction
from finance_tracker_class import FinanceTrackerData
import file_handler
import ui_handler

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
        action = ui_handler.menu(action)
        print(action)
        ACTIONS[action](tracker_data)

    ui_handler.farewell()

def add_transaction():
    pass

def edit_transaction():
    pass

def all_transactions():
    pass

def statistics():
    pass

def generate_report():
    pass

def exit_program(tracker_data):
    file_handler.save_data(tracker_data)

if __name__ == "__main__":
    main()