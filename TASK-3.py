import random

print("\n" + "=" * 30)
print("       PASSWORD GENERATOR")
print("=" * 30)

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special = "!@#$%^&*"

try:
    length = int(input("\nEnter password length: "))

    if length < 1:
        print("Password length must be greater than 0.")

    else:
        print("\nChoose Password Complexity:")
        print("1. Letters Only")
        print("2. Letters + Numbers")
        print("3. Letters + Numbers + Special Characters")

        choice = input("\nEnter your choice (1-3): ")

        password = ""

        if choice == "1":
            characters = lowercase + uppercase

            for i in range(length):
                password += random.choice(characters)

        elif choice == "2":
            if length < 2:
                print("For option 2, length must be at least 2.")
            else:
                characters = lowercase + uppercase + numbers

                # Guarantee at least one number
                password = random.choice(numbers)

                for i in range(length - 1):
                    password += random.choice(characters)

                password = list(password)
                random.shuffle(password)
                password = "".join(password)

        elif choice == "3":
            if length < 4:
                print("For option 3, length must be at least 4.")
            else:
                characters = lowercase + uppercase + numbers + special

                # Guarantee one of each type
                password += random.choice(lowercase)
                password += random.choice(uppercase)
                password += random.choice(numbers)
                password += random.choice(special)

                for i in range(length - 4):
                    password += random.choice(characters)

                password = list(password)
                random.shuffle(password)
                password = "".join(password)

        else:
            print("Invalid choice! Please select 1, 2, or 3.")

        if password != "":
            print("\n" + "-" * 40)
            print("Generated Password:", password)
            print("-" * 40)

except ValueError:
    print("Please enter a valid number.")