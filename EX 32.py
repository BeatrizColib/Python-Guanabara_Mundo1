import calendar
year = int(input("Enter a year: "))
leapyear = calendar.isleap(year)
if leapyear == True:
    print("This year is a leap year! In february we have an extra day!")
else:
    print("This year isn't a leap year. In february we only have 28 days.")
print(calendar.month(year,2))

print(calendar.calendar(year))
print(calendar.monthrange(year,5))
print(calendar.weekday(year,5,21))
