print('Informe a base da potenciação')
base = int(input())

print('Informe o expoente da potenciação')
expoente = int(input())

i = expoente
potencia = 1

if (expoente == 0):
    print('Resultado = 1')
elif (expoente > 0):
    while i > 0:
        potencia *= base
        i -= 1
    print('Resultado =', potencia)
else:
    print('Não calculamos potências com o expoente negativo')