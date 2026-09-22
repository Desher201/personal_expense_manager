import json
from pathlib import Path


class Expense:
    id = 0
    expense_path = Path("expenses.json")

    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category
        Expense.id += 1
        self.id = Expense.id

    def save_expense(self):
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


# expense = Expense("expense", 1, "expense")
# expense_2 = Expense("expense_2", 1, "expense_2")
#
# expense.save_expense()
# expense_2.save_expense()
