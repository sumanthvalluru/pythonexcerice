# Create a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# Print the original tuple
print("Original Tuple:", my_tuple)

# Accessing elements in a tuple
first_element = my_tuple[0]
last_element = my_tuple[-1]

print("First Element:", first_element)
print("Last Element:", last_element)

# Slicing a tuple
sliced_tuple = my_tuple[2:5]
print("Sliced Tuple:", sliced_tuple)

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# Unpacking a tuple
x, y, z = tuple1
print("Unpacked Values:", x, y, z)

# Checking if an element exists in a tuple
element_to_check = 'b'
if element_to_check in tuple2:
    print(f"{element_to_check} is present in the tuple.")
else:
    print(f"{element_to_check} is not present in the tuple.")
