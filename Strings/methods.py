phrase="Giraffe Academy"
print(phrase.lower()) # Converts the string to lowercase
print(phrase.upper()) # Converts the string to uppercase
print(phrase.isupper()) # Checks if the string is in uppercase
print(phrase.islower()) # Checks if the string is in lowercase
print(phrase.upper().isupper()) # Converts the string to uppercase and then checks if it is in uppercase 
# Indexing 
print(phrase[0]) # Prints the first character of the string
# Index function
print(phrase.index("G")) # Prints the index of the first occurrence of "G"
# replace function
print(phrase.replace("Giraffe", "Elephant")) # Replaces "Giraffe" with "Elephant"

# Whenever we have to print a number in a string, we have to converrt it to string
# Example:
print("Giraffe Academy is " + str(10) + " times better than Giraffe Academy")