'''num = (input("Digite um número entre 0 e 9999: "))
n = str(num)
print("Unidade: {}".format((n)[3]))
print("Dezena: {}".format((n)[2]))
print("Centena: {}".format((n)[1]))
print("Milhar: {}".format((n)[0]))'''

num = int(input("digite um número de 0 a 9999: "))
u= num // 1 % 10
d= num //10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("a unidade é {}".format(u))
print("a dezena é {}".format(d))
print("a centena é {}".format(c))
print(("o milhar é {}".format(m)))
