#Write a program to prompt user to enter userid and password. After verifying
#userid and password display a 4 digit random number and ask user to enter the
#same. If user enters the same number then show him success message otherwise
#failed. (Something like captchcorrect
# 

#import random
import random

# Predefined userid and password
USERID = "neha"
PASSWORD = "1234"

#  Ask user for login
uid = input("Enter User ID: ")
pwd = input("Enter Password: ")

if uid == USERID and pwd == PASSWORD:
    #  Generate random 4-digit captcha
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
    
    #  Ask user to enter captcha
    user_captcha = int(input("Enter the captcha: "))
    
    # Verify captcha
    if user_captcha == captcha:
        print("✅ Login Successful!")
    else:
        print("❌ Failed! Wrong captcha.")
else:
    print("❌ Invalid UserID or Password.")
