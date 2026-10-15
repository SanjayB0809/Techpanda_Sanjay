def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    if num2 == 0:
        return "Number Cannot Divide by zero"
    else:
        return num1 / num2

def main():
    while True:
        print("\n===== CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "5":
            print("Calculator closed.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice!")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            print("Result:", add(num1,num2))
        elif choice == "2":
            print("Result:", sub(num1,num2))
        elif choice == "3":
            print("Result:", mul(num1,num2))
        elif choice == "4":
            print("Result:", div(num1,num2))

if __name__ == "__main__":
    main()
