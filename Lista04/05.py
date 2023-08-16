moto = 0
carro = 0
onibus = 0 
lucro = 0

i = 0

while i < 400:
    print('Ocorreu entrada de qual veículo? \n1. Moto \n2. Carro \n3. Ônibus')
    opcao = int(input())

    if (opcao == 1):
        moto += 1
        lucro += 4
    elif (opcao == 2):
        carro += 1
        lucro += 8
    else:
        onibus += 1
        lucro += 20

    i += 1

print('Lucro =', lucro)