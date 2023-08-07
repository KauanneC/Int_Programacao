print('Escolha uma figurra geométrica: \n1. Retângulo \n2. Triângulo \n3. Círculo')
fig = int(input())

if (fig == 1):
    print('Informe a lagura do retângulo: ')
    larg = float(input())
    print('Informe a altura do retângulo: ')
    alt = float(input())
    area = larg * alt
    print('A área do retângulo é: ' + str(area))
elif (fig == 2):
    print('informe a base do triângulo: ')
    base = float(input())
    print('Informe a altura do triângulo: ')
    alt = float(input())
    area = (base * alt) / 2
    print('A área do triângulo é: ' + str(area))
else:
    print('Informe o raio do círculo: ')
    raio = float(input())
    area = 3.14 * (raio * raio)
    print('A área do círculo é: ' + str(area))