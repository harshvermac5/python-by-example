import random

#select the range of number to ask from
def pick_num():
    low = int(input("Enter the bottom of the range: "))
    high = int(input("Enter the top of the range: "))
    comp_num = random.randint(low, high)
    return comp_num

#taking user guess
def first_guess():
    guess = int(input("I am thinking of a number: "))
    return guess

#checking user guess and delivering suggestions
def check_answer(comp_num, guess):
    try_again = True
    while try_again == True:
        if comp_num == guess:
            print("Correct, my love.")
            try_again = False
        elif comp_num>guess:
            guess = int(input("Too low, try again: "))
        else:
            guess = int(input("Too high, try again: "))

#defining a function to call all the previous one
def main():
    comp_num = pick_num()
    guess = first_guess()
    check_answer(comp_num,guess)

#calling the function itself
main()