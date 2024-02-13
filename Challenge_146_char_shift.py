#creating a list of Alphabets
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

#defining a function to get and arrange the data in desired order
def get_data():
    word = input("Enter your message: ")
    word = word.lower()
    num = int(input("Enter a number between 1-26: "))
    #checking and asking for valid number
    if num > 26 or num == 0:
        while num > 26 or num == 0:
            num = int(input("Out of range, Enter a valid number: "))
    data = (word, num)
    return(data)

#defining a fuction to actually shift the data in desired order
def make_code(word, num):
    new_word = ""
    #getting the index of every character entered
    for x in word:
        y = alphabet.index(x)
        #incrementing the index
        y= y+num
        if y > 26:
            #adjusting the bleed, 27 to counteract 0 as index
            y = y-27
        char = alphabet[y]
        new_word = new_word + char
    print()
    print(f"Your Code is {new_word}")
    print()

#defining a function, to reverse the code
def decode(word, num):
    #initalising an empty string
    new_word = ""
    for x in word:
        #getting index of every character in the code
        y = alphabet.index(x)
        y = y-num
        # correcting the bleed
        if y < 0:
            y = y+27
        #getting the values of original string, from alphabet list
        char = alphabet[y]
        # adding the data into the string
        new_word = new_word+char
    print()
    print(f"Your original code was {new_word}")
    print()

#main function to ask for the input
def main():
    again = True
    while again == True:
        print("1. Make a code")
        print("2. Decode a message")
        print("3. Quit")
        print()
        selection = int(input("Enter your selection: "))
        if selection == 1:
            (word, num) = get_data()
            make_code(word,num)
        elif selection == 2:
            (word, num) - get_data()
            decode(word, num)
        elif selection == 3:
            again = False
        else:
            print("Incorrect Selection")

# running the main function predominately
main()