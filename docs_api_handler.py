import gspread
from google.oauth2.service_account import Credentials

def call_api(transactions):
    scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
    ]

    creds = Credentials.from_service_account_file("credentials.json", scopes = scopes)
    client = gspread.authorize(creds)

    workbook_id = "1uM4SfZ4xxMUEpN0DkTyAp4C4al1sZWtkacb46Zjcv7c"
    workbook = client.open_by_key(workbook_id)

    pass_data(workbook, transactions)

def pass_data(workbook, transactions):
    data = [t.to_list() for t in transactions]
    data_sheet = workbook.sheet1
    print("Loading...")
    data_sheet.clear()
    headers = ["Transaction ID", "Amount", "Transaction Type", "Category", "Date"]
    data_sheet.append_row(headers)
    data_sheet.append_rows(data)
    input("Report generated. Press 'Enter' to continue.")
