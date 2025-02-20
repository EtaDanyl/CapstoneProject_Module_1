import uuid
from datetime import datetime

class Transaction:
    def __init__(self, amount: float, transaction_type: str, category: str, date: str = None, transaction_id: str = None):
        """
        Initialize a Transaction object.
        :param amount: The transaction amount (positive for income, negative for expenses if needed).
        :param transaction_type: Type of transaction ('income' or 'expense').
        :param category: Category of the transaction (e.g., 'Food', 'Rent').
        :param date: Date of the transaction (default: current date if not provided).
        :param transaction_id: Unique identifier (default: generated UUID if not provided).
        """
        self._amount = amount
        self._transaction_type = transaction_type.lower()
        self._category = category
        self._date = date if date else datetime.now().strftime("%Y-%m-%d")
        self._transaction_id = transaction_id if transaction_id else str(uuid.uuid4())

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount: float):
        self._amount = amount

    @property
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type: str):
        self._transaction_type = transaction_type.lower()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category: str):
        self._category = category

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date: str):
        self._date = date

    @property
    def transaction_id(self):
        return self._transaction_id

    def __str__(self):
        return f"Transaction(ID: {self.transaction_id}, Amount: {self.amount}, Type: {self.transaction_type}, Category: {self.category}, Date: {self.date})"

    def to_dict(self):
        """ Convert the transaction to a dictionary for easier file storage. """
        return {
            "transaction_id": self.transaction_id,
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "category": self.category,
            "date": self.date
        }
