##   WAP to print all integers  upto n arent  divisible by 2 and 3

# Input n
n = int(input("Enter the value of n: "))

i = 1  # start from 1

print("Numbers not divisible by 2 and 3 up to", n, ":")
while i <= n:
    if i % 2 != 0 and i % 3 != 0:
        print(i, end=" ")
    i += 1
