from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Menu:
    """
    A class containing predefined menu options for a finance tracking application.

    Attributes:
        main (ClassVar[list[str]]): The main menu options.
        editing (ClassVar[list[str]]): Options available in the transaction editing menu.
        filtering_sorting (ClassVar[list[str]]): Options for filtering and sorting transactions.
    """

    main: ClassVar[list[str]] = [
        "Add Transaction",
        "Edit Transaction",
        "All Transactions",
        "Statistics",
        "Generate a Report",
        "Exit",
    ]
    
    editing: ClassVar[list[str]] = [
        "Amount",
        "Type",
        "Category",
        "Date",
        "Delete transaction",
        "Save and Back",
    ]
    
    filtering_sorting: ClassVar[list[str]] = [
        "Amount",
        "Type",
        "Category",
        "Date",
        "Back",
    ]