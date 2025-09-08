

# Input range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Armstrong numbers between {start} and {end} are:")

num = start
while num <= end:
    temp = num
    sum_of_powers = 0
    # count number of digits
    n_digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** n_digits
        temp //= 10

    if sum_of_powers == num:
        print(num, end=" ")

    num += 1
##WAP to print Armstrong number within a given range