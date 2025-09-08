##S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
a = int(input("Enter value of a: "))

s = 0
for i in range(1, 11):
    s += (a ** i) / i

print("Sum of series =", s)

