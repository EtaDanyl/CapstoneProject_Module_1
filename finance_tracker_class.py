from dataclasses import dataclass, field
from transaction_class import Transaction

@dataclass
class FinanceTrackerData:
    """
    A class to manage and analyze financial transactions.
    This class maintains a list of transactions and provides methods 
    to calculate total income, total expenses, and the overall balance.

    Attributes:
        transactions (list[Transaction]): A list of Transaction objects representing financial records.
    Methods:
        total_income() -> float:
            Calculates and returns the total income from all transactions.

        total_expenses() -> float:
            Calculates and returns the total expenses from all transactions.

        total_balance() -> float:
            Computes the net balance by adding total income and total expenses.

        __str__() -> str:
            Returns a formatted string summarizing income, expenses, 
            balance, and savings rate.
    """
    transactions: list[Transaction] = field(default_factory=list)
    
    def total_income(self) -> float:
        return sum(t.amount for t in self.transactions if t.transaction_type == 'income')
    
    def total_expenses(self) -> float:
        return sum(t.amount for t in self.transactions if t.transaction_type == 'expense')
    
    def total_balance(self) -> float:
        return self.total_income() + self.total_expenses()
    
    def __str__(self) -> str:
        total_income = self.total_income()
        total_expenses = self.total_expenses()
        balance = self.total_balance()
        savings_rate = (total_income - total_expenses) / total_income * 100 if total_income > 0 else 0
        
        return (
            f"Total Income: €{total_income:,.2f}\n"
            f"Total Expenses: €{total_expenses:,.2f}\n"
            f"Total Balance: €{balance:,.2f}\n"
            f"Savings Rate: {savings_rate:.2f}%\n"
        )