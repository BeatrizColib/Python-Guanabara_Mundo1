n1=str(input("primeiro aluno: "))
n2=str(input("segundo aluno: "))
n3=str(input("terceiro aluno: "))
n4=str(input("quarto aluno: "))
import random
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print("A ordem dos alunos é {}".format(lista))