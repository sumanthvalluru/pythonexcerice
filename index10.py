class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        # Split the string into words
        words = self.input_string.split()

        # Reverse the order of words
        reversed_words = words[::-1]

        # Join the reversed words to form the final string
        reversed_string = ' '.join(reversed_words)

        return reversed_string

# Example usage:
if __name__ == "__main__":
    input_string = "Hello World! This is a sample string."
    
    # Create an instance of StringReverser
    reverser = StringReverser(input_string)
    
    # Call the reverse_words method
    reversed_result = reverser.reverse_words()

    # Print the result
    print("Original String: ", input_string)
    print("Reversed String: ", reversed_result)
