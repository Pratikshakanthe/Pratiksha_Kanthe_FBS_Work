## WAP to print all even numbers until n

# Program to print even numbers until n

n = int(input("Enter the value of n: "))

print("Even numbers up to", n, "are:")
i = 2   # start from the first even number
while i <= n:
    print(i)
    i += 2   # increase by 2 each time

    