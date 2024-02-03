#defining a function to ask value when called
def ask_value():
    x = int(input("Enter a number: "))
    return x

#defining a function to count, using while loop
def count(num):
    n = 1
    while n<=num:
        print(n)
        n = n+1

#defining a new function to call both the above function at once
def main():
    num = ask_value()
    count(num)

#calling the function
main()