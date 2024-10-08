'''cidade = str(input("qual o nome da sua cidade? "))
cid = (cidade.find('Santo'))
cid2= (cidade.find('santo'))
if cid == -1 and cid2 == -1:
    print("Sua cidade não começa com Santo")
else:
    print("Sua cidade começa com Santo")'''

cidade = str(input("Qual sua cidade: ")).strip().capitalize()
print("Sua cidade começa com 'Santo'? {}".format(cidade[:5] == 'Santo'))
