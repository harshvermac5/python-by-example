import random

# Function to select a random combination of four colors
def select_col():
    colors = ["r", "b", "o", "y", "p", "q", "w"]
    c1 = random.choice(colors)
    c2 = random.choice(colors)
    c3 = random.choice(colors)
    c4 = random.choice(colors)
    return c1, c2, c3, c4  # Return the selected colors as a tuple

# Function to prompt the user to enter their guesses and compare them with the correct combination
def tryit(c1, c2, c3, c4):
    colors = ["r", "b", "o", "y", "p", "q", "w"]
    
    print("The colors are: (r)ed, (b)lue, (o)range, (y)ellow, (p)ink, (q)reen, (w)hite.")

    # Input validation loop for each position
    while True:
        u1 = input("Enter your choice for place 1: ").lower()
        if u1 not in colors:
            print("Incorrect Selection")
        else:
            break

    while True:
        u2 = input("Enter your choice for place 2: ").lower()
        if u2 not in colors:
            print("Incorrect Selection")
        else:
            break

    while True:
        u3 = input("Enter your choice for place 3: ").lower()
        if u3 not in colors:
            print("Incorrect Selection")
        else:
            break

    while True:
        u4 = input("Enter your choice for place 4: ").lower()
        if u4 not in colors:
            print("Incorrect Selection")
        else:
            break

    # Print the correct answers (randomly selected combination)
    print()
    print(f"The correct answers were {c1}, {c2}, {c3}, {c4}")

    # Initialize counters for correct and wrong-place guesses
    correct = 0
    wrong_place = 0

    # Compare each guess with the correct combination and update counters
    if c1 == u1:
        correct += 1
    elif c1 == u2 or c1 == u3 or c1 == u4:
        wrong_place += 1

    if c2 == u2:
        correct += 1
    elif c2 == u1 or c2 == u3 or c2 == u4:
        wrong_place += 1

    if c3 == u3:
        correct += 1
    elif c3 == u2 or c3 == u1 or c3 == u4:
        wrong_place += 1

    if c4 == u4:
        correct += 1
    elif c4 == u2 or c4 == u3 or c4 == u1:
        wrong_place += 1

    # Print the number of correct and wrong-place guesses
    print(f"Correct color in correct place: {correct}.")
    print(f"Correct color in wrong place: {wrong_place}.")

    return correct, wrong_place  # Return the number of correct and wrong-place guesses

# Function to orchestrate the game
def main():
    c1, c2, c3, c4 = select_col()  # Select a random combination of colors
    score = 0
    play = True

    # Game loop
    while play:
        correct, _ = tryit(c1, c2, c3, c4)  # Call tryit() to compare guesses and update score
        score += 1
        if correct == 4:  # Exit the loop if all guesses are correct
            play = False

    print("You Win!")
    print(f"You took {score} guesses.")

# Call the main function to start the game
main()
