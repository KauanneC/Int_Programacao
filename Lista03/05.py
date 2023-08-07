print('Digite um número')
num = int(input())

# num é múltiplo de 2, então, 2 é divisor de num | A divisão entre num e 2 tem de ser exata
if (num%2 ==  0) and (num%3 == 0):
    print('O número é múltiplo de 2 e 3')
else:
    print('O número não é múltiplo de 2 e 3')