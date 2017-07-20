# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

input_string= input("Enter the string to return the characters: ")

#v=("a","e","i","o","u")
vowels=frozenset("aeiou")
characters= set()

for i in input_string:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        characters.add(i)

print(sorted(characters.difference(vowels)))