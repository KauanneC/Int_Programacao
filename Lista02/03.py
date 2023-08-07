print('Qual veículo o Sr. Wayne usou? \n1. Morcego Preto \n2. Vampiro Voador')
tipo_carro = int(input())

if (tipo_carro == 1):
    total = 300 + ((295/16) * 0.75)
    print('Total gasto: R$ %.2f' % (total))
else:
    gasolina = (295/11) * 0.75
    total = 500 + gasolina
    print('Total gasto: R$ %.2f' % (total))