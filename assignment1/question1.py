# WAP to calculate the percentage of student based on marks of any 5 subjects

phy = int(input("Enter marks in Physics: "))
chem = int(input("Enter marks in Chemistry: "))
math = int(input("Enter marks in Mathematics: "))
bio = int(input("Enter marks in Biology: "))
comp = int(input("Enter marks in Computer Science: "))
total_marks = phy + chem + math + bio + comp
percentage = total_marks/500 * 100
print (percentage, "%" )