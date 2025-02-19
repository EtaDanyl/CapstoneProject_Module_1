from transaction_class import Transaction
from finance_tracker_class import FinanceTrackerData
import file_handler
import ui_handler

def main():
    data = file_handler.load_data()
    tracker_data = FinanceTrackerData(data)
    run_tracker(tracker_data)

def run_tracker(tracker_data):
    ui_handler.greet()

    action = 0
    while action != 6:
        ui_handler.print_menu(action + 1)
        
    ui_handler.farewell()

if __name__ == "__main__":
    main()