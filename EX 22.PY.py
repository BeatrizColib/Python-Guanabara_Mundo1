nome = str(input('Digite seu nome: '))
print(nome.upper())
print((nome.lower()))
print(len(nome.replace(' ','')))

nomeseparado = (nome.split())
primeironome = print(len(nomeseparado[0]))

#ou

#primeiro = print(len(nome.split()[0])))

#ou

name = str(input('Seu nome: ')).strip()
print("Seu nome todo maiúsculo é: {}".format(name.upper()))
print("Seu nome todo minúsculo é: {}".format(name.lower()))
print("A quantidade de caracteres é: {}".format(len(name.replace(" ",""))))
print("A quant. de caract. é {}".format(len(name) - name.count(" ")))
print("Seu primeiro nome tem: {} caracteres.".format(len(name.split()[0])))
