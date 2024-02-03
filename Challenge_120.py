import random

def addition():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    print(num1, "+", num2, "=")
    user_answer = int(input("Your answer: "))
    actual_answer = num1 + num2
    answers = (user_answer, actual_answer)
    return answers

def subtraction():
    num1 = random.randint(20, 50)
    num2 = random.randint(5, 20)
    print(num1, "-", num2, "=")
    user_answer = int(input("Your answer: "))
    actual_answer = num1 - num2
    answers = (user_answer, actual_answer)
    return answers

def check_answer(user_answer, actual_answer):
    if user_answer == actual_answer:
        print("You're correct, my love")
    else:
        print(f"Sorry dear, the answer is {actual_answer}")

def main():
    print("1. Addition")
    print("2. Subtraction")
    selection = int(input("Enter your selection: 1 or 2"))
    if selection == 1:
        user_answer, actual_answer = addition()
        check_answer(user_answer, actual_answer)
    elif selection == 2:
        user_answer, actual_answer = subtraction()
        check_answer(user_answer, actual_answer)
    else:
        print("Incorrect selection.")

main()
