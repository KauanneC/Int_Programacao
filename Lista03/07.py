print("Digite um número inteiro")
num = int(input())

res = 1

while num >= 1:
    res *= num   # res = res * num
    num -= 1     # num = num - 1

print(res)