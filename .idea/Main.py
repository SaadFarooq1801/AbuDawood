import Addition
import difference
import product
import division

def main():
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
    print("\n--- Calculation Summary ---")
    print(f"Addition of {num1} and {num2} is: {Addition.addition(num1,num2)}")
    print(f"Subtraction of {num2} from {num1} is: {difference.difference(num1,num2)}")
    print(f"The product of {num1} and {num2} is: {product.product(num1,num2)}")
    print(f"The quotient of {num1} by {num2} is: {division.division(num1,num2)}")
    print("---------------------------")


# Run the main function
if __name__ == "__main__":
    main()