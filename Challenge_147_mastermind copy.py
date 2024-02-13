import random

def select_col():
    """Selects a random combination of colors."""
    colors = ["r", "b", "o", "y", "p", "q", "w"]
    return tuple(random.choice(colors) for _ in range(4))

def tryit(correct_combination):
    """Allows the user to guess the combination."""
    colors = ["r", "b", "o", "y", "p", "q", "w"]
    print("The colors are: (r)ed, (b)lue, (o)range, (y)ellow, (p)ink, (g)reen, (w)hite.")
    
    guess = [input(f"Enter your choice for the place {i+1}").lower() for i in range(4)]
    
    correct = sum(1 for g, c in zip(guess, correct_combination) if g == c)
    wrong_place = sum(min(guess.count(c), correct_combination.count(c)) for c in set(guess)) - correct

    print()
    print(f"Correct color in correct place are {correct}.")
    print(f"Correct color in wrong place are {wrong_place}.")
    print()
    return correct, wrong_place

def main():
    """Main function to run the game."""
    correct_combination = select_col()
    score = 0
    
    while True:
        correct, _ = tryit(correct_combination)
        score += 1
        if correct == 4:
            break

    print("You Win!")
    print(f"You took {score} guesses.")

if __name__ == "__main__":
    main()
