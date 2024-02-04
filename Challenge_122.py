import csv

#defining a function which asks the data and add to predefined target file
def addtofile():
    file = open("Salaries.csv","a")
    name = input("Enter name: ")
    salary = input("Enter Salary: ")
    newrecord = name+ ", " +str(salary)+"\n"
    file.write(str(newrecord))
    file.close()

#print each line of the targeted file
def viewrecords():
    file = list(csv.reader(open("Salaries.csv")))
    for row in file:
        print(row)
    file.close()

#Creating a Loop to run the program as long as user don't quit
tryagain = True
while tryagain == True:
    print("1. Add to file")
    print("2. View all record")
    print("3. Quit program")
    # print()
    selection = input("Enter the number of your selection: ")
    if selection == "1":
        addtofile()
    elif selection == "2":
        viewrecords()
    elif selection == "3":
        tryagain = False
    else:
        print("Incorrect option")