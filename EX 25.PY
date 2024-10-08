'''nome = str(input("Qual seu nome? ")).strip().title()
n = nome.find('Silva')
if n == -1:
    print("Seu nome não tem 'Silva'")
else:
    print("Seu nome tem 'Silva'")'''

#ou

name = str(input("Qual seu nome? ")).strip().title()
print("Seu nome tem Silva? {}.".format('Silva' in name))