##check prime number or not

n = int(input("enter the number:"))

i = 2

while i < n and n % i != 0:
    i += 1

if i == n:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")

