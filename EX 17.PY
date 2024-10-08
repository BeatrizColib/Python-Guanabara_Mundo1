import math

co=float(input("digite o cateto oposto: "))
ca=float(input("digite o cateto adjacente: "))
from math import hypot
h= math.hypot(co,ca)
print("A hipotenusa é {:.2f}".format(h))