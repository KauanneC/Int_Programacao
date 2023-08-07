print('Informe o primeiro número: ')
num1 = int(input())

print('Informe o segundo número: ')
num2 = int(input())

if (num2%2 == 0):
    print('A soma dos números é: ' + str(num1 + num2))
else:
    print('A multiplicação dos números é: ' + str(num1 * num2))