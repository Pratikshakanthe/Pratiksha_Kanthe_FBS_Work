##Write a program to check if given 3 digit number is a palindrome or not.
# for the integer
num = (input(" enter the number"))
# reverse the number
rev = int(str(num)[::-1])

if num == rev:
    print(num, "is a Palindrome")
else:
    print(num, "is Not a Palindrome")
    
    ## both
    # WAP to check if input (string or number) is palindrome

value = input("Enter a number or string: ")

# Convert everything to string for checking
if value == value[::-1]:
    print(value, "is a Palindrome")
else:
    print(value, "is Not a Palindrome")
    
    ### for the string use (text)
    # WAP to check if a string is palindrome or not

text = input("Enter a string: ")

if text == text[::-1]:
    print(text, "is a Palindrome")
else:
    print(text, "is Not a Palindrome")


