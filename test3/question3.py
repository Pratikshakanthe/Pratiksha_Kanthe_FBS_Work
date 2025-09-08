##WAP to accept basic salary if basic salary is below 20000 then da = 10% and 12% ta hra 15% otherwise hra = 20% da = 15% ta = 18%
##based on this calculate total salary  of each emp and also total salary of all emp



n = int(input("Enter number of employees: "))

allemp_salary = 0  # total salary of all employees

for i in range(1, n+1):
    basic = float(input("Enter basic salary of employee:"))

    if basic < 20000:
        da = 0.10 * basic
        ta = 0.12 * basic
        hra = 0.15 * basic
    else:
        da = 0.15 * basic
        ta = 0.18 * basic
        hra = 0.20 * basic

    total_salary = basic + da + ta + hra
    print("Total salary of employee:" , total_salary)

    allemp_salary += total_salary

print("Total salary of all employees:" ,allemp_salary)

    
    