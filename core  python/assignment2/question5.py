# (5 ) WAP to calculate celling price of book based on the cost price and discount

cost_price = int(input("enter the price of book:"))
D = int(input("enter the discount on book:"))
discount = cost_price * D / 100
selling_price = cost_price - discount

print(discount)
print(selling_price)


