import csv

# opening password file, and putting making it a list
def get_data():
    # try and except block for error handling
    try:
        with open("passwords.csv", "r") as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        print("Password file not found.")
        return []

# function that takes existing user data as parameter for checking duplicates, otherwise returns the Input data
def create_userID(user_data):
    while True:
        userID = input("Enter a new user ID: ")
        userID_lower = userID.lower()
        if any(userID_lower == existing[0] for existing in user_data):
            print(f"{userID} has already been allocated.")
        else:
            return userID

# Lists and test the requirements of Having a password, only returns the password if all test are passed
def create_password():
    while True:
        password = input("Enter Password: ")
        if len(password) < 8:
            print("Password should be at least 8 characters long.")
        elif not any(char.isupper() for char in password):
            print("Password should contain at least one uppercase letter.")
        elif not any(char.islower() for char in password):
            print("Password should contain at least one lowercase letter.")
        elif not any(char.isdigit() for char in password):
            print("Password should contain at least one digit.")
        else:
            return password

# searches the user id in the existing database "user_data" taking it as parameter
def find_userID(user_data):
    while True:
        searchID = input("Enter the user ID you're looking for: ")
        searchID_lower = searchID.lower()
        if any(searchID_lower == existing[0] for existing in user_data):
            return searchID
        else:
            print(f"{searchID} is not in the list.")

# function that takes two values, a search from the function above and existing database as parameters, then updates the passwords which is located in 2nd column and finally overwrites the file with new data
def change_password(userID, user_data):
    for i, data in enumerate(user_data):
        if data[0] == userID:
            # placing the updated password in the second column of the "user_data"
            user_data[i][1] = create_password()
            with open("passwords.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(user_data)
            print("Password updated successfully.")
            return
    print(f"User ID '{userID}' not found.")

# function that prints all the user ids in the system
def display_all_userID(user_data):
    print("User IDs in the system:")
    # underscore states that passwords are not needed to be printed
    for userID, _ in user_data:
        print(userID)

# initialising the asking prompt that takes input from the user and runs the desired function
def main():
    user_data = get_data()
    while True:
        print("\n1. Create a new User ID")
        print("2. Change a Password")
        print("3. Display all user IDs")
        print("4. Quit")
        # initialising a variable that stores user input
        selection = input("Enter Selection: ")
        if selection == '1':
            new_userID = create_userID(user_data)
            new_password = create_password()
            user_data.append([new_userID, new_password]) # appends the new data to existing data
            with open("passwords.csv", "a", newline='') as file: # newline function ensures the correct handling of append function when using cross platform
                writer = csv.writer(file)
                writer.writerow([new_userID, new_password]) # appends the new data to database
            print("User ID created successfully.")
        elif selection == '2':
            userID = find_userID(user_data)
            change_password(userID, user_data)
        elif selection == '3':
            display_all_userID(user_data)
        elif selection == '4':
            print("Quitting...")
            break
        else:
            print("Incorrect selection. Please try again.")

# running the main function of the code
if __name__ == "__main__":
    main()

# for my future understanding
'''The block `if __name__ == "__main__":` is a common Python idiom used to check whether the script is being run as the main program or if it is being imported as a module into another script. 

Here's what it means:

- `__name__` is a special built-in variable in Python that stores the name of the current module. When the Python interpreter runs a script, it sets the `__name__` variable for that script to `"__main__"` if it is the main program being executed.

- The expression `__name__ == "__main__"` checks if the current module is being run as the main program. If it is, the expression evaluates to `True`. If the module is being imported as a module into another script, `__name__` will be set to the module's name, and the expression will evaluate to `False`.

- `main()` is a function call. In this context, it typically refers to the main entry point of the script, where the main functionality of the program is executed.

Putting it all together:

- `if __name__ == "__main__":` ensures that the code inside the block is only executed if the script is being run directly as the main program.

- `main()` is called inside this block, indicating that when the script is run directly, it will execute the `main()` function, which likely contains the primary functionality of the program.

This structure allows the script to have reusable functions and classes that can be imported into other scripts without running the main part of the program, providing modularity and flexibility in Python applications.'''