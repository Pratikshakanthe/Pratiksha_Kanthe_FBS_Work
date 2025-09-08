##c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

n = int(input("Enter n: "))

geo_sum = 0
term = 1
for i in range(n):
    geo_sum += term
    term *= 2

print("Sum of geometric series =", geo_sum)
