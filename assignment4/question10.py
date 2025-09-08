##WAP to check if given number is Perfect Number.

# Input number
n = int(input("Enter a number: "))

i = 1
sum_of_divisors = 0

while i < n:
    if n % i == 0:        # if i is a divisor
        sum_of_divisors += i
    i += 1

if sum_of_divisors == n:
    print(n, "is a Perfect Number")
else:
    print(n, "is not a Perfect Number")
