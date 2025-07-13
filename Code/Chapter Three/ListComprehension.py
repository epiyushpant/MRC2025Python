# Write program to apply list comprehension.
# Initialize a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use list comprehension to create a new list with squares of even numbers
squared_evens = [x**2 for x in numbers if x % 2 == 0]

# Print the result
print("Original numbers:", numbers)

print("Squared even numbers:", squared_evens)

# Use list comprehension to create a new list with cubes of odd numbers
cubed_odds = [x**3 for x in numbers if x % 2 != 0]
# Print the result
print("Cubed odd numbers:", cubed_odds) 

# Use list comprehension to create a new list with numbers greater than 5
greater_than_five = [x for x in numbers if x > 5]
# Print the result
print("Numbers greater than 5:", greater_than_five)

# Use list comprehension to create a new list with numbers multiplied by 2
multiplied_by_two = [x * 2 for x in numbers]
# Print the result
print("Numbers multiplied by 2:", multiplied_by_two)

# Use list comprehension to create a new list with strings of numbers
string_numbers = [str(x) for x in numbers]
# Print the result
print("String representation of numbers:", string_numbers)
# Use list comprehension to flatten a 2D list

two_d_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened_list = [item for sublist in two_d_list for item in sublist]

# Print the result
print("Flattened 2D list:", flattened_list)

# Use list comprehension to create a new list with the length of each string in a list
string_list = ["apple", "banana", "cherry"]
lengths = [len(s) for s in string_list]
# Print the result
print("Lengths of strings:", lengths)

# Use list comprehension to create a new list with the first letter of each string in a list
first_letters = [s[0] for s in string_list]
# Print the result
print("First letters of strings:", first_letters)
# Use list comprehension to create a new list with the last letter of each string in a list
last_letters = [s[-1] for s in string_list]

# Print the result
print("Last letters of strings:", last_letters)
# Use list comprehension to create a new list with the reversed strings
reversed_strings = [s[::-1] for s in string_list]
# Print the result
print("Reversed strings:", reversed_strings)

# Use list comprehension to create a new list with the uppercase version of each string
uppercase_strings = [s.upper() for s in string_list]
# Print the result
print("Uppercase strings:", uppercase_strings)

# Use list comprehension to create a new list with the lowercase version of each string
lowercase_strings = [s.lower() for s in string_list]
# Print the result
print("Lowercase strings:", lowercase_strings)

# Use list comprehension to create a new list with the strings that contain the letter 'a'
strings_with_a = [s for s in string_list if 'a' in s]

# Print the result
print("Strings containing 'a':", strings_with_a)
# Use list comprehension to create a new list with the strings that start with 'b'

strings_starting_with_b = [s for s in string_list if s.startswith('b')]
# Print the result
print("Strings starting with 'b':", strings_starting_with_b)
# Use list comprehension to create a new list with the strings that end with 'e'
strings_ending_with_e = [s for s in string_list if s.endswith('e')]

# Print the result
print("Strings ending with 'e':", strings_ending_with_e)
# Use list comprehension to create a new list with the strings that have more than 5 characters
long_strings = [s for s in string_list if len(s) > 5]
# Print the result
print("Strings with more than 5 characters:", long_strings)
# Use list comprehension to create a new list with the strings that have less than 5 characters
short_strings = [s for s in string_list if len(s) < 5]
# Print the result
print("Strings with less than 5 characters:", short_strings)

# Use list comprehension to create a new list with the strings that have exactly 5 characters
exactly_five_characters = [s for s in string_list if len(s) == 5]
# Print the result
print("Strings with exactly 5 characters:", exactly_five_characters)

# Use list comprehension to create a new list with the strings that have vowels
strings_with_vowels = [s for s in string_list if any(vowel in s for vowel in 'aeiou')]

# Print the result
print("Strings with vowels:", strings_with_vowels)
# Use list comprehension to create a new list with the strings that have consonants
strings_with_consonants = [s for s in string_list if any(consonant in s for consonant in 'bcdfghjklmnpqrstvwxyz')]
# Print the result
print("Strings with consonants:", strings_with_consonants)