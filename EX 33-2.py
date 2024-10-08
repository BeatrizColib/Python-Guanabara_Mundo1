a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero: "))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > c and b > c:
    maior = b
if c > a and c > b:
    maior = c

print("Maior: {} \nMenor: {}".format(maior, menor))
