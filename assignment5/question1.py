#Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.


# Set correct credentials

correct_id = "prati"
correct_password = "12345"


# Allow up to 3 attempts
attempts = 0
while attempts < 3:
    id = input("Enter User ID: ")
    password = input("Enter Password: ")

    if id == correct_id and password == correct_password:
        print("Login successful! ✅")
        break
    else:
        print("Invalid UserID or Password. Try again.\n")
        attempts += 1

if attempts == 3:
    print("Too many failed attempts. Program terminated ❌")
