#In this copy of code, I have substituted the creating counter then iterating list, for enumerate function

#defining a function that asks for a name, then appends it on the list
def add_name():
    name = input("Enter a name: ")
    names.append(name)
    return names

#defining a funciton that presents a enumerated list, and then updates it by asking a new term in that place
def change_name():
    for num, x in enumerate(names):
        print(num, x)
    select_num = int(input("Enter the number of the name you want to change: "))
    name = input("Enter the new name: ")
    names[select_num]= name
    return names

#defining a function that presents a enumerated list, which then delete the data at specified index
def delete_name():
    for num, x in enumerate(names):
        print(num, x)
    select_num = int(input("Enter the number of the name you want to delete: "))
    try:
        names.pop(select_num)
    except IndexError:
        print("Invalid index. Please try again.")
    return names

#function that prints each item in the list
def view_names():
    for x in names:
        print(x)
    print()

#a main function that applies logic and bring other function to work
def main():
    again = "y" #creates an endless loop, running until user selects to quit
    while again == "y":
        print("1) Add a name")
        print("2) Change a name")
        print("3) Delete a name")
        print("4) View names")
        print("5) Quit")
        selection = int(input("what do you want to do? "))
        if selection == 1:
            names == add_name()
        elif selection == 2:
            names == change_name()
        elif selection == 3:
            names == delete_name()
        elif selection == 4:
            names == view_names()
        elif selection == 5:
            again = "n"
        else:
            print("Incorrect option: ")
        data = (names, again)

names = []
main()