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

secret_number = input("Set a secret number, I'll guess it!")
while not (secret_number.isdigit() or (secret_number.startswith('-') and secret_number[1:].isdigit())):
    secret_number = input("Secret number can be a positive or negative whole number")
else:
    secret_number = int(secret_number)

user_name = input("Provide your name")

guess_number = input("Guess the secret number")
while not (guess_number.isdigit() or (guess_number.startswith('-') and guess_number[1:].isdigit())):
    guess_number = input("Secret number was a positive or negative whole number")
else:
    guess_number = int(guess_number)

count_guess_cycle = 1
while guess_number != secret_number:
    count_guess_cycle += 1
    guess_number = input("Guess the secret number")
    while not (guess_number.isdigit() or (guess_number.startswith('-') and guess_number[1:].isdigit())):
        guess_number = input("Secret number was a positive or negative whole number")
    else:
        guess_number = int(guess_number)

print(f"{count_guess_cycle} guessed the number")
