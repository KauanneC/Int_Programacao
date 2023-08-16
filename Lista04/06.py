# 6 números distintos 1 a 60
import random

i = 0

while i < 5:
    num1 = random.randint(1,60)
    num2 = random.randint(1,60)
    num3 = random.randint(1,60)
    num4 = random.randint(1,60)
    num5 = random.randint(1,60)
    num6 = random.randint(1,60)

    while (num2 == num1) or (num2 == num3) or (num2 == num4) or (num2 == num5) or (num2 == num6):
        num2 = random.randint(1,60)

    while (num3 == num1) or (num2 == num3) or (num3 == num4) or (num3 == num5) or (num3 == num6):
        num3 = random.randint(1,60)

    while (num4 == num1) or (num4 == num2) or (num4 == num3) or (num4 == num5) or (num4 == num6):
        num4 = random.randint(1,60)

    while (num5 == num1) or (num5 == num2) or (num5 == num3) or (num5 == num4) or (num5 == 6):
        num5 = random.randint(1,60)

    while (num6 == num1) or (num6 == num2) or (num6 == num3) or (num6 == num4) or (num6 == num5):
        num6 = random.randint(1,60)
    
    i += 1

    print('Palpite', i,'= [', num1 , ',', num2 , ',', num3 , ',', num4 , ',', num5 , ',', num6 ,']')