i = 1
sinal = 1
soma = 0

print('S = ', end='')

while i < 51:
    if (sinal == 1) or (sinal == 2):
        print(' -', i, end='')
        soma -= i
        sinal += 1
    elif (sinal == 3):
        print(' +', i, end='')
        soma += i
        sinal += 1
    else:
        print(' +', i, end='')
        soma += i
        sinal = 1
    
    i += 1

print('\nS =', soma)