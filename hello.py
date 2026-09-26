import json
from  datetime import datetime
expenses = []
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def show_expenses():
    if not expenses:
        print("No expenses found")
        return
    for expense in expenses:
        print(f"Name: {expense['name']} | Cost:{expense['cost']} | Date: {expense['date']}")    
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
         json.dump(expenses, file, indent=4)      
def add_expense( ):
    name = input("Expense name : ")
    cost = float(input("Cost: "))
    date = datetime.now().strftime("%Y_%m_%d")
    expens = {"name": name, "cost": cost, "date": date}
    expenses.append(expens)
    save_expenses(expenses)
    print("Expense added!")
expenses = load_expenses()
while True:
    print("1.Add expense") 
    print("2.Show_expenses")
    print("3.Exit") 
    choice =input("choose: ") 
    if choice == "1" :
        add_expense()
    elif choice == "2":
        show_expenses() 
    elif choice == "3":
        break       
