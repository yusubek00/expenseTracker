import json


def addExpense(expensesList):

    # Prompt user for expense details
    expenseName = input("Expense Name: ")

    while True:
        try:
            price = float(input("Price: "))
            break
        except ValueError:
            print("Pllease enter a valid number")
    
    categoriesList = ["Food", "Transport", "Bills", "Entertainment", "Shopping", "Health", "Other"]
    start = 1
    for category in categoriesList:
        print(f"{start}. {category}")
        start += 1

    choice = int(input("Choose category: "))
    chosenCategory = categoriesList[choice - 1]
    

    # Generate a unique ID for the new expense
    if expensesList:
        newId = max(expenseEntry["id"] for expenseEntry in expensesList) + 1
    else:
        newId = 1


    expense = {
        "id" : newId,
        "name" : expenseName,
        "price" : price,
        "category" : chosenCategory
    }

    return expense

def viewExpenses():
    return loadExpenses()

def loadExpenses(): # Load all previous expenses 
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    

def saveExpenses(expensesList): # Save expenses list onto a file
    with open("expenses.json", "w") as f:
        json.dump(expensesList, f, indent=2)



def main():
    # List of all expense entries
    expensesList = loadExpenses()


    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            expensesList.append(addExpense(expensesList))
            
            # Save expensesList into a file
            saveExpenses(expensesList)

            print(expensesList)  
            print(type(expensesList[0]["price"]))          
        
        elif choice == "2":
            print(viewExpenses()) 
            
        elif choice == "3":
            break



if __name__ == "__main__":
    main()
