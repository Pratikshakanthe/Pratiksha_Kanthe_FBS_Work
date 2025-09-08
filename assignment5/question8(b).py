##b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

N = int(input("Enter N: "))

power_sum = 0
for i in range(1, N+1):
    power_sum += N ** i

print("Sum of powers =", power_sum)
