#(10) WAP to accept an integer amount from user and tell minimum number of notes needed for representing that amount 

amount = int(input("Enter the amount: "))

notes = [ 1000, 500, 200, 100 ]

print("Minimum notes required:")

for note in notes:
    count = amount // note   
    if count > 0:
        print(note, "x", count)
    amount = amount % note  