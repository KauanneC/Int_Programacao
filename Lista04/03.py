import random

num1 = random.randint(1,29)
num2 = random.randint(1,29)
num3 = random.randint(1,29)

while (num1 == num2):
    num2 = random.randint(1,29)

while (num3 == num1) or (num3 == num2):
    num3 = random.randint(1,29)

print('Terra 01:', num1, '\nTerra 02:', num2, '\nTerra 03:', num3)