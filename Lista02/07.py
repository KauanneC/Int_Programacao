print('Informe o Lado A do triangulo: ')
lado_A = float(input())

print('Informe o Lado B do triangulo: ')
lado_B = float(input())

print('Informe o Lado C do triangulo: ')
lado_C = float(input())

if (lado_A > (lado_B + lado_C)):
    print('Não é um triangulo')
elif (lado_B > (lado_A + lado_C)):
    print('Não é um triangulo')
elif (lado_C > (lado_A + lado_B)):
    print('Não é um triangulo')
else:
    print('É um triângulo')

    if (lado_A == lado_B and lado_B == lado_C):
        print('Triângulo Equilátero')
    elif (lado_A == lado_B or lado_B == lado_C or lado_A == lado_C):
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')