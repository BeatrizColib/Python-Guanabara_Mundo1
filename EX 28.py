import random
from time import sleep
number = random.randint(0,5)

num = int(input("Choose a number between 0 and 5: "))
print("Thinking...")
sleep(3)

if num == number:
    print("You're right! Congratulations!")
else:
    print("You're wrong!")