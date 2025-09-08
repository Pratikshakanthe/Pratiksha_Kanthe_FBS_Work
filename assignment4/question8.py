##WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

i = start

print("Numbers divisible by 7 and multiple of 5 in the given range:")
while i <= end:
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=" ")
    i += 1
