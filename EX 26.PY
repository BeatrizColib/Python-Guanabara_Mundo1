frase = str(input("digite sua frase: ")).upper().strip()
print("A letra 'a' aparece {} vezes".format(frase.count('A')))
print("A primeira letra 'a' aparece na posiçao {}".format(frase.find('A')+1))
print("A última letra 'a' aparece na posiçao {}".format(frase.rfind('A')+1))
