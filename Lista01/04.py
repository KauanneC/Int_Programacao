import random

esqueleto = random.randint(20,80)
corcunda = random.randint(20,80)
ortodontista = 20
mulher = random.randint(20, 80)
senhora = 20
atleta = random.randint(20,50)

if (esqueleto + corcunda + ortodontista + mulher) - (senhora + atleta) > 120:
    print("A porta foi aberta")
else:
    print("A porta não foi aberta")