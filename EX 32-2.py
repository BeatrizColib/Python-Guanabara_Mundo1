from datetime import date
year = int(input("Enter a year: "))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("This year is a leap year!")
else:
    print("This year isn't a leap year!")