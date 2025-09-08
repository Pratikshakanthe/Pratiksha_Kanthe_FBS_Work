#write a progarm to print n prime numbers

n = int(input("Enter how many prime numbers: "))
num = 2
count = 0

while count < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count += 1
    num += 1
