## fibonacci series
# Program to print Fibonacci series up to n terms

n = int(input("Enter number of terms: "))

a = 0   # first term
b = 1   # second term
i = 0   # counter

print("Fibonacci series:")
while i < n:
    print(a, end=" ")   # print current number
    c = a + b           # next term is sum of previous two
    a = b               # shift: second becomes first
    b = c               # next becomes second
    i += 1              # increase counter
