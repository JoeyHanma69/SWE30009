# factorial.py

def recur_factorial(n):
    """Recursively calculates the factorial of a number."""
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


# Remove the input part for testing purposes.
# You can keep this part if running the script directly
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        print("The factorial of", num, "is", recur_factorial(num))
