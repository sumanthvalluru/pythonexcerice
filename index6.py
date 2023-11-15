# Function to find the largest of three numbers
def find_largest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Example usage
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

largest_number = find_largest_number(number1, number2, number3)
print(f"The largest number among {number1}, {number2}, and {number3} is: {largest_number}")