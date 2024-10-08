'''import math
n= float(input("Digite um ângulo: "))
seno = math.sin(math.radians(n))
cosseno = math.cos(math.radians(n))
tangente = math.tan(math.radians(n))

print("Angulo: {}, Seno {:.2f}, Cosseno {:.2f}, Tangente {:.2f}".format(n,seno,cosseno,tangente))'''

from math import radians,sin,cos,tan
angulo=float(input("Digite o angulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print("O angulo {:.0f} tem: \n o seno {:.2f}, \n o cosseno {:.2f}, \n a tangente {:.2f}".format(angulo,seno,cosseno,tangente))

