distance = float(input("What is the distance in kilometers between the departure and the destination of the trip? "))
if distance <= 200:
    price = distance * 0.5
    print("The ticket fare is $ {:.2f}".format(price))
else:
    price = distance * 0.45
    print("The ticket fare is $ {}".format(price))

# outra forma

distance1 = float(input("What is the distance in kilometers between the departure and the destination of the trip? "))
price1 = distance1 * 0.5 if distance1 <= 200 else distance1 * 0.45
print("The price is $ {}".format(price1))