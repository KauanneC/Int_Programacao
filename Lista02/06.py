print('Informe o valor da Hipotenusa')
hipotenusa = int (input())

print('Informe o valor do primeiro cateto')
cateto1 = int (input())

print('Informe o terceiro valor')
cateto2 = int (input())

if ((hipotenusa*hipotenusa) == (cateto1*cateto1) + (cateto2*cateto2)):
    print('É um triângulo retângulo')
else:
    print('Não é um triângulo retângulo')