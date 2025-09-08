##Accept no. of passengers from user and per ticket cost. Then accept age of each
##passenger and then calculate total amount to ticket to travel for all of them based on
#following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.
n = int(input(" Enter the  no of passengers:-"))
cost = int(input(" Enter the cost:-"))

Total_amount = 0

for i in range(n):
    age = int(input("Enter the age of passenger"))
    
if age < 12:  # Children get 30% discount
        fare = ticket_cost * 0.7
elif age > 59:  # Senior citizens get 50% discount
        fare = ticket_cost * 0.5
else:  # Others pay full price
        fare = ticket_cost
 