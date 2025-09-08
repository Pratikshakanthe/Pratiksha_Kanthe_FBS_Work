### WAP to print all numbers in a range divisible by a given number.


start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
divisor = int(input("Enter the number to divide by: "))

i = start

print(f"Numbers divisible by {divisor} in the range {start} to {end}:")
while i <= end:
    if i % divisor == 0:
        print(i, end=" ")
    i += 1
