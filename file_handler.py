from transaction_class import Transaction
import json
import os
from typing import List
from datetime import datetime

def load_data(filename="transactions_data.json") -> List[Transaction]:
    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        return []

    with open(filename, 'r') as file:
        if not os.path.exists(filename) or os.stat(filename).st_size == 0:
            return []  

        with open(filename, 'r') as file:
            json_data = json.load(file)
            return [from_dict(data) for data in json_data]

def from_dict(data) -> Transaction:
    return Transaction(
        amount = data['amount'],
        transaction_type = data['transaction_type'],
        category = data['category'],
        date = datetime.strptime(data['date'], "%Y-%m-%d").date(),
        transaction_id = data['transaction_id']
    )

def save_data(transactions: List[Transaction], filename="transactions_data.json"):
    with open(filename, 'w') as file:
        json_data = [to_dict(transaction) for transaction in transactions]
        json.dump(json_data, file, indent=4)

def to_dict(transaction: Transaction) -> dict:
    return {
        'amount': transaction._amount,
        'transaction_type': transaction._transaction_type,
        'category': transaction._category,
        'date': str(transaction._date),
        'transaction_id': transaction._transaction_id
    }