#WAP to to enter P, T, R, and calculate compound interest
P = int(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = int(input("Enter Time: "))

CI = P * (1 + R/100) ** T - P

print("Compound Interest =", CI)