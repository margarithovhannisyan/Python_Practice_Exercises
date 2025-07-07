'''
homework5
● Create a script that gets the full name, balance, expense, and active loan balance of a customer
● Calculate and print the balance after the expense.
● If the customer spends from the loan, then tell about it
● Do necessary checks.
● Print in a readable and nice format
'''

ERROR_MESSAGE = "Provided value is not a valid"
full_name = input("Please provide customer full name")

balance = input("Please provide balance amount")
while not balance.replace(",", "", 1).isdigit():
    print(ERROR_MESSAGE)
    balance = input("Please provide balance amount")
else:
    balance = float(balance)

expense = input("Please provide expense amount")
while not expense.replace(",", "", 1).isdigit():
    print(ERROR_MESSAGE)
    expense = input("Please provide expense amount")
else:
    expense = float(expense)

active_loan_balance = input("Please provide active loan balance")
while not active_loan_balance.replace(",", "", 1).isdigit():
    print(ERROR_MESSAGE)
    active_loan_balance = input("Please provide active loan balance")
else:
    active_loan_balance = float(active_loan_balance)

if balance - expense < 0:
    if balance+active_loan_balance-expense < 0:
        missed_amount=expense-balance-active_loan_balance
        print(f"Error: Dear {full_name}, you still need {missed_amount} amount to cover your expenses")
    else:
        active_loan_balance = active_loan_balance + balance - expense
        print(f"Warning: Dear {full_name}, your loan balance is being used, new loan balance is {active_loan_balance}")
else:
    balance = balance - expense
    print(f"Dear {full_name}, after spending {expense} amount, your new balance is {balance}")