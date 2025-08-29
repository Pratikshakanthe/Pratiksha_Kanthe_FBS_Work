#question - 3

#(3)convert distant given in feet and inches into meter and centimeter:-

feet = int(input("Enter distance in feet: "))
inches = int(input("Enter remaining inches: "))

total_inches = (feet * 12) + inches
centimeters = total_inches * 2.54
meters = centimeters / 100

print(f'{centimeters}', "centimeters",  {meters}, "meters")