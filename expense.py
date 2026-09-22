import json
from pathlib import Path
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filename="expense.log",
    encoding="utf8"
)


class Expense:
    id = 0
    expense_path = Path("expenses.json")

    def __init__(self, name:str, amount:int, category:str):
        self.name:str = name
        self.amount:int = amount
        self.category:str = category
        Expense.id += 1
        self.id = Expense.id

    def save_expense(self) -> None:
        if self.expense_path.exists():
            with open(self.expense_path, "r", encoding="utf8") as file:
                try:
                    data = json.load(file)
                except Exception:
                    data = []
        else:
            data = []


        data.append({
            "id": self.id,
            "name": self.name,
            "amount": self.amount,
            "category": self.category

        })

        with open(self.expense_path, "w", encoding="utf8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            logging.info(f"Saved expense: {self.id}")

# expense = Expense("expense", 1, "expense")
# expense_2 = Expense("expense_2", 1, "expense_2")
#
# expense.save_expense()
# expense_2.save_expense()
