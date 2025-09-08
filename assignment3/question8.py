#Input 5 subject marks from user and display grade(eg.First class,Second class ..)
math = int(input("enter the math marks"))
phy = int(input("enter the math phy"))
bio = int(input("enter the math bio"))
hindi =  int(input("enter the math hindi"))
sci = int(input("enter the math sci"))

if math < 35 or phy < 35 or bio < 35 or hindi < 35 or  sci < 35 :
      print("fail")
else:
    
     total_marks = math + phy + bio +  hindi + sci
     percentage = total_marks / 500 * 100
     print("percentage:", percentage)

     if (percentage >= 75):
         print("first class destination : A grade")
     elif(percentage >= 60):
         print("first class  :  B grade")
     elif(percentage >= 45):
         print("second class : C garde")
     elif(percentage >= 35):
         print("third class: D garde")
     else:
         print("fail")    
    
