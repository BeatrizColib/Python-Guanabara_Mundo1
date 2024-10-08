salary = float(input("What is the salary? "))
if salary > 1250:
    increase1 = salary * 1.1
    print("You'll receive a 10% raise, your new salary is $ {:.2f}".format(increase1))
else:
    increase2 = salary * 1.15
    print("You'll receive a 15% raise, your new salary is $ {:.2f}".format(increase2))