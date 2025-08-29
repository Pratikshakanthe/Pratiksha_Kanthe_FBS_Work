#(1)convert the time entered in hh , min , sec into seconds:-


h = int(input("Enter hours: "))
m = int(input("Enter minutes: "))
sec = int(input("Enter seconds: "))


total_seconds = (h * 3600) + (m* 60) + sec
    

print("Total seconds:", total_seconds)
