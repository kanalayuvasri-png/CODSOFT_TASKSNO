print("\n" + "=" * 30)
print("       MINI CALCULATOR")
print("=" * 30)

while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 5:
        print("\nThank you for using Mini Calculator!")
        break

    elif choice >= 1 and choice <= 4:

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == 1:
            print(f"\nResult: {a} + {b} = {a + b}")

        elif choice == 2:
            print(f"\nResult: {a} - {b} = {a - b}")

        elif choice == 3:
            print(f"\nResult: {a} × {b} = {a * b}")

        elif choice == 4:
            if b == 0:
                print("\nError: Division by zero is not possible.")
            else:
                print(f"\nResult: {a} ÷ {b} = {a / b}")

    else:
        print("\nInvalid choice! Please select 1-5.")