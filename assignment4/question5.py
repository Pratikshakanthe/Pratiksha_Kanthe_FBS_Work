## fibonacci series
# Program to print Fibonacci series up to n terms

n = int(input("Enter number of terms: "))

a = -1  # first term
b = 1   # second term
i = 0   # counter

print("Fibonacci series:")
while i < n:
    c = a + b  
    print(c, end=" ")   # print current numbe          # next term is sum of previous two
    a = b               # shift: second becomes first
    b = c               # next becomes second
    i += 1              # increase counter
    
    
## using for loop
#for i in range (n):