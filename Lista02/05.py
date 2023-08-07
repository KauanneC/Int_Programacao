import random

print('Quantos votos teve Naruto Uzumaki?')
votos_naruto = int(input())
#votos_naruto = random.randint(0,100)
#print(votos_naruto)

print('Quantos votos teve Sakura Haruno?')
votos_sakura = int(input())
#votos_sakura = random.randint(0,100)
#print(votos_sakura)

print('Quantos votos teve Shino Aburame?')
votos_shino = int(input())

print('Quantos votos brancos?')
votos_brancos = int(input())

print('Quantos votos nulos?')
votos_nulos = int(input())

if ((votos_naruto + votos_sakura + votos_shino) > (votos_brancos + votos_nulos)): 
    print('Eleição Válida')
    if ((votos_naruto > votos_sakura) and (votos_naruto > votos_shino)):
        print('Naruto é o vencedor!')
    elif ((votos_sakura > votos_naruto) and (votos_sakura > votos_shino)):
        print('Sakura é a vencedora!')
    elif ((votos_shino > votos_naruto) and (votos_shino > votos_sakura)):
        print('Shino é o vencedor!')
    elif ((votos_naruto == votos_sakura) and (votos_sakura > votos_shino)):
        print('Empate entre Naruto e Sakura')
    elif ((votos_sakura == votos_shino) and (votos_shino > votos_naruto)):
        print('Empate entre Sakura e Shino')
    elif ((votos_naruto == votos_shino) and (votos_shino > votos_sakura)):
        print('Empate entre Naruto e Shino')
    else:
        print('Empate entre todos!!')
else:
    print('Eleição Inválida')