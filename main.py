import json
from expense import Expense
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filename="expense.log",
    encoding="utf-8"
)

while True:
    print(f"1. Додати витрату"
          "\n2. Показати всі витрати"
          "\n3. Показати витрати за категорією"
          "\n4. Показати загальну суму"
          "\n5. Вийти")
    choice = input()

    if choice == "1":
        name = input("Введіть назву:")
        while True:
            amount = input("Введіть суму:")
            try:
                amount = int(amount)
                break
            except ValueError:
                print("Сума має бути int")
                continue
        category = input("Введіть категорію")
        expense = Expense(name, int(amount), category)
        expense.save_expense()

    elif choice == "2":
        with open("expenses.json", "r", encoding="utf8") as file:
            try:
                data = json.load(file)
                print(f"{"Всі витрати" :=^50}")
                for i in data:
                    print(f"{i["id"]}. {i["name"]:20} {i["amount"]} грн {i["category"]}")
                print(f"=" * 50)
                logging.info(f"Вивелося: {len(data)} витрат")
            except json.JSONDecodeError:
                print(f"=" * 50)
                print(f"Витрат нема")
                print(f"=" * 50)
                logging.info(f"Вивелося: 0 витрат")

    elif choice == "3":
        category = input("Введіть назву категорії")
        with open("expenses.json", "r", encoding="utf8") as file:
            try:
                data = json.load(file)
                for i in data:
                    list_of_expenses = []
                    if i["category"] == category:
                        list_of_expenses.append(i)
                if list_of_expenses:
                    print(f"{f"Всі витрати категорії:{category}" :=^50}")
                    for i in list_of_expenses:
                        print(f"{i["id"]}. {i["name"]:20} {i["amount"]} грн {i["category"]}")
                    print(f"=" * 50)
                else:
                    print(f"=" * 50)
                    print("Витрат такої категорії немає")
                    print(f"=" * 50)

            except json.JSONDecodeError:
                print("Витрат такої категорії немає")



    elif choice == "4":
        suma = 0
        with open("expenses.json", "r", encoding="utf8") as file:
            try:
                data = json.load(file)
                for i in data:
                    suma += int(i["amount"])
            except json.JSONDecodeError:
                pass
        print("="*50)
        print("Загальна сума:",suma)
        print("="*50)
    elif choice == "5":
        logging.info(f"Програму завершено")
        break
    else:
        print("Невірне введення")
        logging.info("Невірне введення")
        continue
