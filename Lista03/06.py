mega = 1

while mega < 7:
    print("Digite um número")
    num = int(input())
    
    if num > 60 or num < 0:
        print("Esse número não é válido")
    else:
        print("Esse número é válido")
    
    mega += 1