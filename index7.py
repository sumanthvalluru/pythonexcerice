# Function to print a star pattern
def print_star_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

# Example usage
num_rows = int(input("Enter the number of rows for the star pattern: "))
print_star_pattern(num_rows)