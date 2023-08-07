print('Informe sua idade')
idade = int (input())

if (idade >= 18):
    total = ((idade - 17) * 365) * 2
    print('Quantidade de água: ' + str(total))
else:
    print('Você não é adulto.')