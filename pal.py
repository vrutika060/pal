
# Program to check whether a string is a palindrome

text = input("Enter a string: ")

reverse_text = text[::-1]

if text.lower() == reverse_text.lower():
    print(text, "is a Palindrome")
else:
    print(text, "is not a Palindrome")

