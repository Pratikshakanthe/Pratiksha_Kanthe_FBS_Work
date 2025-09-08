##x - x2/3 + x3/5 - x4/7 + .... to n terms

x = int(input("Enter x: "))

s = 0
sign = 1
den = 1

for i in range(1, 10):
    s += sign * (x ** i) / den
    sign *= -1        # change sign
    den += 2          # odd denominators

print("Sum of series =", s)
