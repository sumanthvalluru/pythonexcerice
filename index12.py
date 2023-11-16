class IntegerToRomanConverter:
    def int_to_roman(self, num):
        # Define the mapping of Roman numerals and their corresponding values
        roman_numerals = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
        ]

        # Initialize an empty string to store the Roman numeral representation
        result = ""

        # Iterate through the Roman numerals
        for roman, value in roman_numerals:
            # Repeat the Roman numeral while the value is less than or equal to num
            while num >= value:
                result += roman
                num -= value

        return result

# Example usage:
if __name__ == "__main__":
    # Create an instance of IntegerToRomanConverter
    converter = IntegerToRomanConverter()

    # Test cases
    num1 = 3549
    num2 = 1998
    num3 = 49

    # Convert integers to Roman numerals
    result1 = converter.int_to_roman(num1)
    result2 = converter.int_to_roman(num2)
    result3 = converter.int_to_roman(num3)

    # Print results
    print(f"{num1} in Roman numerals: {result1}")
    print(f"{num2} in Roman numerals: {result2}")
    print(f"{num3} in Roman numerals: {result3}")
