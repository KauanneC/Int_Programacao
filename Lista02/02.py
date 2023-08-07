print('Informe seu sexo. Digite: \n1. Feminino \n2. Masculino')
sexo = int(input())

print('Informe sua altura: ')
alt = float(input())

f = (62.1 * alt) - 44.7
m = (72.2 * alt) - 58

if (sexo == 1):
    print('Seu peso ideal é: ' + str(f))
else:
    print('Seu peso ideal é: ' + str(m))