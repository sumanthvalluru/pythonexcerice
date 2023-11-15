# Create a list
my_list = [1, 2, 3, 4, 5]

# Print the original list
print("Original List:", my_list)

# Append elements to the list
my_list.append(6)
my_list.append(7)

# Print the list after appending elements
print("List after appending elements:", my_list)

# Remove elements from the list
element_to_remove = 3
if element_to_remove in my_list:
    my_list.remove(element_to_remove)
    print(f"Element {element_to_remove} removed from the list.")
else:
    print(f"Element {element_to_remove} not found in the list.")

# Print the list after removing elements
print("List after removing elements:", my_list)