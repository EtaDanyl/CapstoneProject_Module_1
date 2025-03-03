import gspread
from google.oauth2.service_account import Credentials
import json
import webbrowser


def load_config():
    with open("config.json") as config_file:
        return json.load(config_file)

def call_api(transactions):
    config = load_config()
    workbook_id = config.get("WORKBOOK_ID")
    scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
    ]
    creds = Credentials.from_service_account_file("credentials.json", scopes = scopes)
    client = gspread.authorize(creds)
    workbook = client.open_by_key(workbook_id)
    pass_data(workbook, transactions)
    webbrowser.open(config.get("SHEET_LINK"))

def pass_data(workbook, transactions):
    data = [t.to_list() for t in transactions]
    data_sheet = workbook.sheet1
    print("Loading...")
    data_sheet.clear()
    headers = ["Transaction ID", "Amount", "Transaction Type", "Category", "Date"]
    data_sheet.append_row(headers)
    data_sheet.append_rows(data)
    input("Report generated. Press 'Enter' to continue.")

