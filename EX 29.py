speed = float(input("What is the speed of the car (km/h)? "))
if speed <= 80:
    print("You're within the allowed speed limit")
else:
    violation = (speed - 80) * 7.00
    print("Fined! You exceeded the allowed speed limit and will have to pay a $ {:.2f} fine.".format(violation))