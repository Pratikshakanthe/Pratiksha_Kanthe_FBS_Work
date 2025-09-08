##WAP to  check if user has entererd correct userid and password

correct_userid = "pratiksha"
correct_password = "123456"

userid = input("enter the userid:")
password = input("enter the password:")

if (userid == correct_userid ) and (password == correct_password):
    print("login successfully")
else:
    print("invalid userid and passowrd")


