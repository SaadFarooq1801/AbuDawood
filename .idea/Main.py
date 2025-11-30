## Simplified Python Program to Input Two Integers

def get_two_integers():
    """
    Prompts the user to enter two whole numbers (integers).
    Assumes valid integer input.
    """
    # 1. Get the first integer input
    # Use int() to convert the input string directly to an integer
    num1 = int(input("Please enter the first whole number: "))

    # 2. Get the second integer input
    num2 = int(input("Please enter the second whole number: "))

    # 3. Print the results and a simple calculation
    print("\n--- Input Summary ---")
    print(f"You entered the first integer: {num1}")
    print(f"You entered the second integer: {num2}")
    print("---------------------")

# Run the main function
if __name__ == "__main__":
    get_two_integers()