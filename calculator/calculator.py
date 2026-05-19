print("=" * 30)
print("      CALCULATOR")
print("=" * 30)

while True:

    try:

        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose Operation")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (**)")

        choice = input("Enter choice: ")

        if choice == "1":
            print(f"\nResult: {num1 + num2}")

        elif choice == "2":
            print(f"\nResult: {num1 - num2}")

        elif choice == "3":
            print(f"\nResult: {num1 * num2}")

        elif choice == "4":

            if num2 == 0:
                print("\nCannot divide by zero")

            else:
                print(f"\nResult: {num1 / num2}")

        elif choice == "5":
            print(f"\nResult: {num1 % num2}")

        elif choice == "6":
            print(f"\nResult: {num1 ** num2}")

        else:
            print("\nInvalid choice")

    except:
        print("\nInvalid input. Enter numbers only.")

    again = input("\nDo another calculation? (yes/no): ")

    if again.lower() != "yes":
        print("\nCalculator Closed")
        break