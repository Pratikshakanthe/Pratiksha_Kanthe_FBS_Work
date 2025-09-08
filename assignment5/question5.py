#Write a program to accept an integer amount from user and tell minimum
#number of notes needed for representing that amount. (Use looping to optimize
#the problem)
amount = int(input("Enter the amount:-"))
notes = [ 2000, 1000 , 500 , 200 , 100 , 50 , 20 ,10 ]


print("Minimum notes required:")

for note in notes:
    if amount >= note:
        count = amount // note       # number of this note
        amount = amount % note       # remaining amount
        print(note, "x", count)

