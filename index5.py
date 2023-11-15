# Create a dictionary
my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York',
    'grades': {'math': 90, 'english': 85, 'history': 92}
}

# Print the original dictionary
print("Original Dictionary:", my_dict)

# Accessing values in a dictionary
name = my_dict['name']
age = my_dict['age']
city = my_dict['city']
print("Name:", name)
print("Age:", age)
print("City:", city)

# Accessing values in nested dictionaries
math_grade = my_dict['grades']['math']
history_grade = my_dict['grades']['history']
print("Math Grade:", math_grade)
print("History Grade:", history_grade)

# Adding a new key-value pair to the dictionary
my_dict['occupation'] = 'Engineer'
print("Dictionary after adding a new key-value pair:", my_dict)

# Modifying a value in the dictionary
my_dict['age'] = 26
print("Dictionary after modifying the 'age' value:", my_dict)

# Removing a key-value pair from the dictionary
if 'grades' in my_dict:
    del my_dict['grades']
    print("Dictionary after removing the 'grades' key:", my_dict)
else:
    print("'grades' key not found in the dictionary.")

# Iterating through key-value pairs in the dictionary
print("Iterating through key-value pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
