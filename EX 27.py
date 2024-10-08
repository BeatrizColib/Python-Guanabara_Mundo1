nome = str(input("Digite seu nome completo: ")).title().strip()
n= nome.split()
print("Primeiro nome: {}".format(n[0]))
print("último nome: {}".format(n[len(n)-1]))
print("seu nome tem {} nomes".format(len(n)))

