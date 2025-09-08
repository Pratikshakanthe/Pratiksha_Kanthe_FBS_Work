## sum of series 

# Program to find sum of series 1 + 2 + ... + n

n = int(input("Enter the value of n: "))

sum = 0     # to store the total
i = 1       # starting number

while i <= n:
    sum = sum + i   # add current i to sum
    i = i + 1       # move to next number

print("Sum of series is:", sum)
