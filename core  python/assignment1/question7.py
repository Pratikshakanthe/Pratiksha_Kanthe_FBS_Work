#WAP to convert days into years ,weeks and days

days = int(input(" enter the days:"))

years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7

print(f'years:{years}, weeks:{weeks}, days:{remaining_days}')


