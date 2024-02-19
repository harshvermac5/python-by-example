import random

# function that creates tuple of random colors
def select_col():
    colors = ["r","b","o","y","p","q","w"]
    c1 = random.choice(colors)
    c2 = random.choice(colors)
    c3 = random.choice(colors)
    c4 = random.choice(colors)
    data = (c1,c2,c3,c4)
    return data

# function that takes previously generated tuple as parameters and compares them with user input
def tryit(c1,c2,c3,c4):
    colors = ["r","b","o","y","p","q","w"]
    print("The colors are: (r)ed, (b)lue, (o)range, (y)ellow, (p)ink, (g)reen, (w)hite.")
    try_again = True # creating a loop which asks for user input unless correctly entered
    while try_again == True:
        u1 = input("Enter your choice for the place 1: ")
        u1 = u1.lower()
        if u1 not in colors:
            print("Incorrect Selection")
        else:
            try_again = False
    try_again = True # creating a loop which asks for user input unless correctly entered
    while try_again == True:
        u2 = input("Enter your choice for the place 2: ")
        u2 = u2.lower()
        if u2 not in colors:
            print("Incorrect Selection")
        else:
            try_again = False
    try_again = True # creating a loop which asks for user input unless correctly entered
    while try_again == True:
        u3 = input("Enter your choice for the place 3: ")
        u3 = u3.lower()
        if u3 not in colors:
            print("Incorrect Selection")
        else:
            try_again = False
    try_again = True # creating a loop which asks for user input unless correctly entered
    while try_again == True:
        u4 = input("Enter your choice for the place 4: ")
        u4 = u4.lower()
        if u4 not in colors:
            print("Incorrect Selection")
        else:
            try_again = False
    print(f"The correct answers were {select_col()}")

    
    # initialsing counters for scores
    correct = 0
    wrong_place = 0

    if c1 == u1:
        correct = correct+1
    elif c1 == u2 or c1 == u3 or c1 == u4:
        wrong_place = wrong_place+1
    if c2 == u2:
        correct = correct+1
    elif c2 == u1 or c2 == u3 or c2 == u4:
        wrong_place = wrong_place+1
    if c3 == u3:
        correct = correct+1
    elif c3 == u2 or c3 == u1 or c3 == u4:
        wrong_place = wrong_place+1
    if c4 == u4:
        correct = correct+1
    elif c4 == u2 or c4 == u3 or c4 == u1:
        wrong_place = wrong_place+1

    print()
    print(f"Correct color in correct place are {correct}.")
    print(f"Correct color in wrong place are {wrong_place}.")
    print()
    data2 = [correct, wrong_place]
    return data2

# function that perfoms all the necessary function
def main():
    (c1,c2,c3,c4) = select_col()
    score = 0
    play = True
    while play == True:
        (correct,wrong_place) = tryit(c1,c2,c3,c4)
        score = score + 1
        if correct == 4:
            play = False

    print("You Win!")
    print(f"You took {score} guesses.")

main()