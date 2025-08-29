##Write a program to check if person is eligible to marry or not (male age >=21 and
##female age>=18)

gender = (input("enter the gender:(M/F)"))
age = int(input("enter the age"))

if(gender == 'M') and (gender == 'F'):
    if(age >= 21):
        print(" eligible for marrige")
    else:
        print("not eligible")
else:
    if(age >= 18):
        print("eligible for maarrige")   
    else:
        print("not eligible")
     