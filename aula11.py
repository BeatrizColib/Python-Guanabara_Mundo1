print('\033[4:37:41mHey, Bia! Let`s go study the ANSI standard!\033[m')

print('\033[1:32:44mHello, Bia!\033[m')

number1 = 5
number2 = 3
print(f'The values are \033[32m]{number1}\033[m and \033[35m{number2}\033[m')

name = 'Bia'
print(f'Helo, \033[41:1:30m{name}\033[m. Nice to meet you!')
print('Helo, \033[30m{}\033[m. How are you?'.format(name))

print('-' *70)

collors = {'clear':'\033[m',
           'blue': '\033[34m',
           'yellow': '\033[33m',
           'red':'\033[31m'}
print(collors)

print()
print(f'Helo, {collors['red']} {name} {collors['clear']}. Nice to meet you!')