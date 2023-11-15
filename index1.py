# Function to perform arithmetic operations
def arithmetic_operations(a, b):
    # Addition
    sum_result = a + b
    print(f"Sum: {a} + {b} = {sum_result}")

    # Subtraction
    difference_result = a - b
    print(f"Difference: {a} - {b} = {difference_result}")

    # Multiplication
    product_result = a * b
    print(f"Product: {a} * {b} = {product_result}")

    # Division (result is always a float in Python 3)
    if b != 0:
        division_result = a / b
        print(f"Division: {a} / {b} = {division_result}")
    else:
        print("Cannot divide by zero.")

    # Floor Division (returns the floor of the division)
    if b != 0:
        floor_division_result = a // b
        print(f"Floor Division: {a} // {b} = {floor_division_result}")
    else:
        print("Cannot perform floor division by zero.")

    # Modulus (returns the remainder of the division)
    if b != 0:
        modulus_result = a % b
        print(f"Modulus: {a} % {b} = {modulus_result}")
    else:
        print("Cannot calculate modulus with zero.")

    # Exponentiation
    exponential_result = a ** b
    print(f"Exponentiation: {a} ** {b} = {exponential_result}")


# Example usage
num1 = 10
num2 = 3

arithmetic_operations(num1, num2)