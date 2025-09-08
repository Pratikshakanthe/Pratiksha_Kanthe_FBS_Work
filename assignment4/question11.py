##WAP to check if given number Strong Number

# Input number
n = int(input("Enter a number: "))

temp = n
sum_of_factorials = 0

while temp > 0:
    digit = temp % 10        # extract last digit
    # calculate factorial of digit
    fact = 1
    i = 1
    while i <= digit:
        fact *= i
        i += 1
    sum_of_factorials += fact
    temp //= 10              # remove last digit

if sum_of_factorials == n:
    print(n, "is a Strong Number")
else:
    print(n, "is not a Strong Number")
