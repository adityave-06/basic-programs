def show_menu():
    print("Welcome to the Calculator!")
    print("Please choose an option:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
def getnumbers():
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number :"))
    return a, b
def addition():
    a,b = getnumbers()
    print(f"{a} + {b} = {a+b}")
def subtraction():
    a,b = getnumbers()
    print(f"{a} - {b} = {a-b}")
def multiplication():
    a,b = getnumbers()
    print(f"{a} x {b} = {a*b}")
def division():
    a,b = getnumbers()
    if b == 0:
        print("Division by zero is not allowed.")
    else:
        print(f"{a} / {b} = {a/b}")
def main():
    choice = 0
    while choice != 5:
        show_menu()
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            addition()
        elif choice == 2:
            subtraction()
        elif choice == 3:
            multiplication()
        elif choice == 4:
            division()
        else:
            print("Exiting the program.")
main()
    