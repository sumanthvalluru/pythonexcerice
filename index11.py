class PowerCalculator:
    def power(self, x, n):
        # Base case: when n is 0, return 1
        if n == 0:
            return 1
        
        # Recursively calculate power for n/2 and square the result
        temp = self.power(x, n // 2)
        
        # If n is even
        if n % 2 == 0:
            return temp * temp
        # If n is odd
        else:
            # If n is negative, return 1 / (x * temp * temp)
            if n < 0:
                return 1 / (x * temp * temp)
            # If n is positive, return x * temp * temp
            else:
                return x * temp * temp

# Example usage:
if __name__ == "__main__":
    # Create an instance of PowerCalculator
    calculator = PowerCalculator()

    # Test cases
    x1, n1 = 2, 3
    x2, n2 = 3, -2
    x3, n3 = 4, 0

    # Calculate powers
    result1 = calculator.power(x1, n1)
    result2 = calculator.power(x2, n2)
    result3 = calculator.power(x3, n3)

    # Print results
    print(f"{x1}^{n1} =", result1)
    print(f"{x2}^{n2} =", result2)
    print(f"{x3}^{n3} =", result3)
