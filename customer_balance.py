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

initial_balance = input("Please provide balance amount")
while not initial_balance.replace(",", "", 1).isdigit():
    print(ERROR_MESSAGE)
    initial_balance = input("Please provide balance amount")
else:
    initial_balance = float(initial_balance)

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

new_balance=initial_balance
new_loan_balance=active_loan_balance
used_balance=0
used_loan=0
if initial_balance - expense < 0:
    if initial_balance+active_loan_balance-expense < 0:
        missed_amount=expense-initial_balance-active_loan_balance
        used_balance=initial_balance
        new_balance=0
        used_loan=active_loan_balance
        new_loan_balance=0
        print(f"Error: Dear {full_name}, you still need {missed_amount} amount to cover your expenses")
    else:
        used_balance=initial_balance
        new_balance=0
        new_loan_balance = active_loan_balance + initial_balance - expense
        used_loan=expense-initial_balance
        print(f"Warning: Dear {full_name}, your loan balance is being used, new loan balance is {new_loan_balance}")
else:
    used_balance=expense
    new_balance = initial_balance - expense
    print(f"Dear {full_name}, after spending {expense} amount, your new balance is {new_balance}")

print(f"customer: {full_name} "
    f"\ninitial balance: {initial_balance}"
    f"\nused balance: {used_balance}"
    f"\nnew balance: {new_balance}"
    f"\nexpense: {expense} "
    f"\ninitial loan balance: {active_loan_balance}"
    f"\nused loan: {used_loan}"
    f"\nnew loan balance: {new_loan_balance}")