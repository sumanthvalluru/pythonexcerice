def factorial_recursive(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: factorial(n) = n * factorial(n-1)
    else:
        return n * factorial_recursive(n - 1)

# Example usage:
if __name__ == "__main__":
    # Test case
    number = 7

    # Calculate factorial using recursion
    result = factorial_recursive(number)

    # Print the result
    print(f"The factorial of {number} is: {result}")
