from dataclasses import dataclass, field
from transaction_class import Transaction

@dataclass
class FinanceTrackerData:
    transactions: list[Transaction] = field(default_factory=list)