def get_unique_words(file_path):
    unique_words = set()

    # Open the file and read its content
    with open(file_path, 'r') as file:
        # Split the content into words
        words = file.read().split()

        # Add unique words to the set
        for word in words:
            unique_words.add(word.lower())  # Convert to lowercase to treat words case-insensitively

    return sorted(unique_words)

def main():
    file_path = input("Enter the path to the text file:")

    try:
        unique_words = get_unique_words(file_path)
        
        # Print unique words in alphabetical order
        print("\nUnique words in alphabetical order:")
        for word in unique_words:
            print(word)

    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
