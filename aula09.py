frase = 'bia é a mais linda e esperta  '
print(frase[10])
print(frase[0:5])
print(frase)
print(frase.count("a"))
print(frase.find("bia"))
print(frase.find("Bia"))
print(frase.upper())
print(frase.upper().find("BIA"))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('bia','Beatriz'))
print((frase.capitalize()))
print(frase.title())
print('BIA' in frase)
print(frase.split())


'''Uma string é imutável. Usa-se o replace para conseguir imprimir uma frase de outra forma. Porém se escrever:
frase = "lili e juli sairam"
frase.replace(´lili´,´juju´)
print(frase)

ele imprimirá a frase original, pois o replace nao muda a frase em si, mas gera um novo print dela se eu colocar.
o que imprimiria trocando o lili por juli, seria:
print(frase.replace(´lili´,´juju´)
ou
frase = frase.replace(´lili´,´juju´)
print(frase)
'''


print('oi')

print('Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o'
      ' Fatiamento de String, Análise com len(), count(), find(), '
      'transformações com replace(), upper(), lower(), capitalize(), '
      'title(), strip(), junção com join().')

print('''Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são'
      ' o Fatiamento de String, '
      'Análise com len(), '
      'count(), '
      'find(), '
      'transformações com replace(), '
      'upper(), '
      'lower(), '
      'capitalize(), '
      'title(), '
      'strip(), '
      'junção com join().''')

