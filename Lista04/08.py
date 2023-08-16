# Desafio 01
import random

total = 0
loki01 = random.randint(1,10)
volstagg = random.randint(1,10)

if (loki01 > volstagg):
    total += 1
    print('Loki venceu o desafio 1')
else:
    print('Volstagg venceu o desafio 1')

# Desafio 02
i = 0
loki_res = 0
frandral_res = 0

while i < 10:
    loki02 = random.randint(0,60)
    frandral = random.randint(0,60)

    if (loki02 <= 50):
        loki_res = loki_res + loki02
    
    if (frandral <= 50):
        frandral_res = frandral_res + frandral

    i += 1

if (loki_res < frandral_res):
    total += 1
    print('Loki venceu o desafio 2')
else:
    print('Frandral venceu o desafio 2')

# Desafio 03
loki03 = random.randint(1,2)

if (loki03 == 2):
    total += 1
    print('Loki venceu o desafio 3')
else:
    print('Hogun venceu o desafio 3')

# Desafio 04
turno = 0
num1 = 1
num2 = 0

while (num1 != num2):
    # Loki começa
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)

    if (turno%2 == 0) and (num1 == num2):
        total += 1
        print('Loki venceu o desafio 4')
    
    turno += 1
    
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)

    if (turno%2 != 0) and (num1 == num2):
        print('Valquíria venceu o desafio 4')

# Desafio 05
i = 0 
rodada = 0
pontos_Loki = 0
pontos_Sif = 0

while i < 3:
    # Loki está atacando
    ataque = random.randint(1,50)
    defesa = random.randint(1,50)

    if ((ataque%2 == 0) and (defesa%2 != 0) or (ataque%2 != 0) and (defesa%2 == 0)):
        pontos_Loki += 1
    
    # Lady Sif está atacando
    ataque = random.randint(1,50)
    defesa = random.randint(1,50)

    if ((ataque%2 == 0) and (defesa%2 != 0) or (ataque%2 != 0) and (defesa%2 == 0)):
        pontos_Sif += 1

    i += 1

if (pontos_Loki > pontos_Sif):
    total += 1
    print('Loki venceu o desafio 5')
else:
    print('Lady Sif venceu o desafio 5')

# Final
total += 1 # trapaça

if (total >= 3):
    print('Loki venceu', total, 'guerreiros. \nEle foi escolhido para defender Asgard')
else:
    print('Loki venceu', total, 'guerreiros. \nEle não foi escolhido para defender Asgard')
