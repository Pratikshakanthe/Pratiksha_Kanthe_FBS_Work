###

num = int(input("enter the number:"))

d1 = num  // 100
d2 = (num // 10) % 10
d3 = num % 10
reversed_sum = d1 * 100 + d2 * 10 + d3

print(f'd1:{d1}, d2:{d2}, d3:{d3}')

print(f'sum of digit is:{d1 + d2 + d3}')
