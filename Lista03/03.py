print('Qual foi a profissão sorteada pelo jogador? \n1. Médico \n2. Jornalista \n3. Advogado \n4. Professor \n5. Físico \n6. Comerciante \n7. Estudante')
profissao = int(input())

if (profissao == 1):
    print('Qual foi o caminho escolhido? \n1. Caminho A \n2. Caminho B')
    caminho = int(input())
    if (caminho == 1):
        montante = (50 * 20) + (25 * 10)
        print('Montante final do Médico: R$ %.2f' % (montante))
    else:
        montante = (50 * 20) + (25 * 5)
        print('Montante final do Médico: R$ %.2f' % (montante))
elif (profissao == 2):
    print('Qual foi o caminho escolhido? \n1. Caminho A \n2. Caminho B')
    caminho = int(input())
    if (caminho == 1):
        montante = (24 * 20) + (12 * 10)
        print('Montante final do Jornalista: R$ %.2f' % montante)
    else:
        montante = (24 * 20) + (12 * 5)
        print('Montante final do Jornalista: R$ %.2f' % (montante))
elif (profissao == 3):
    print('Qual foi o caminho escolhido? \n1. Caminho A \n2. Caminho B')
    caminho = int(input())
    if (caminho == 1):
        montante = (50 * 20) + (25 * 10)
        print('Montante final do Advogado: R$ %.2f' % (montante))
    else:
        montante = (50 * 20) + (25 * 5)
        print('Montante final do Advogado: R$ %.2f' % (montante))
elif (profissao == 4):
    print('Qual foi o caminho escolhido? \n1. Caminho A \n2. Caminho B')
    caminho = int(input())
    if (caminho == 1):
        montante = (24 * 20) + (12 * 10)
        print('Montante final do Professor: R$ %.2f' % (montante))
    else:
        montante = (24 * 20) + (12 * 5)
        print('Montante final do Professor: R$ %.2f' % (montante))
elif (profissao == 5):
    print('Qual foi o caminho escolhido? \n1. Caminho A \n2. Caminho B')
    caminho = int(input())
    if (caminho == 1):
        montante = (30 * 20) + (15 * 10)
        print('Montante final do Físico: R$ %.2f' % (montante))
    else:
        montante = (30 * 20) + (15 * 5)
        print('Montante final do Físico: R$ %.2f' % (montante))
elif (profissao == 6):
    print('Qual foi o caminho escolhido? \n1. Caminho A \n2. Caminho B')
    caminho = int(input())
    if (caminho == 1):
        montante = (12 * 20) + (6 * 10)
        print('Montante final do Comerciante: R$ %.2f' % (montante))
    else:
        montante = (12 * 20) + (6 * 5)
        print('Montante final do Comerciante: R$ %.2f' % (montante))
else:
    print('Qual foi o caminho escolhido? \n1. Caminho A \n2. Caminho B')
    caminho = int(input())
    if (caminho == 1):
        montante = (16 * 20) + (8 * 10)
        print('Montante final do Estudante: R$ %.2f' % (montante))
    else:
        montante = (16 * 20) + (8 * 5)
        print('Montante final do Estudante: R$ %.2f' % (montante))