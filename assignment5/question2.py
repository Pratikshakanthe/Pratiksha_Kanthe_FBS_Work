#Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.


n = int(input("Enter number of students: "))  
total_percentage = 0  # To store total percentage

for i in range(n):
    print(f"\nEnter marks for Student {i+1}:")
    total_marks = 0

    # Input 5 subject marks
    for j in range(5):
        marks = int(input(f"\nSubject {j+1}:"))
        total_marks += marks

    # Calculate percentage
    percentage = (total_marks / 500) * 100
    print( "Percentage of student:" ,percentage ," %")

    # Add to total percentage
    total_percentage += percentage

# Calculate average percentage
average = total_percentage / n
print("Average Percentage of Class:" , average , "%")



