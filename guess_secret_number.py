"""
homework 6
Guess the Secret Code
Instructions:
1. Set a secret number (e.g., 42).
2. Ask the user for their name.
3. Use a while loop to ask the user to guess the number.
- Convert input to int.
- Give hints: "Too high", "Too low".
- Break when guessed correctly.
- Skip invalid input (e.g., not a number).
4. Count attempts and display with formatted output:
"Congrats Alice! You guessed the number in 4 attempts."
5. Check type() for dynamic type checking.
"""

def check_if_whole_number(input_number):
    while not (input_number.isdigit() or (input_number.startswith('-') and input_number[1:].isdigit())):
        input_number = input("Number can be a positive or negative whole number")
    else:
        input_number = int(input_number)
    return input_number

secret_number = check_if_whole_number(input("Set a secret number, I'll guess it!"))
user_name = input("Provide your name")
guess_number = check_if_whole_number(input("Guess the secret number"))

count_guess_cycle = 1
while guess_number != secret_number:
    if secret_number - guess_number > 0:
        print("too low")
    else:
        print("too high")
    count_guess_cycle += 1
    guess_number = check_if_whole_number(input("Guess the secret number"))

print(f"Congrats {user_name}! You guessed the number in {count_guess_cycle} attempts.")
