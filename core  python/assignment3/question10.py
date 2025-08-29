#Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

price = float(input("Enter base ticket price per person: "))
total = 0

for i in range(5):
    age = int(input(f"Enter age of person {i+1}: "))
    
    if age < 12:
        fare = price * 0.70     # 30% discount → pay 70%
    elif age > 59:
        fare = price * 0.50     # 50% discount → pay 50%
    else:
        fare = price            # no discount
    
    print(f"Person {i+1} (age {age}) pays: {fare}")
    total += fare               # add to total

print("\nTotal ticket amount =", total)
