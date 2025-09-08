## WAP to calculate the sum of following series where n is input by user 
n = int(input("Enter n: "))

sum_series = 0

fact = 1
for i in range(1, n+1):
    fact = fact * i        
    sum_series += i / fact

print("Sum of series =", sum_series)

