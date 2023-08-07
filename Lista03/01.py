print('Qual foi a nota do(a) aluno(a) em Português?')
port = float(input())

if (port >= 8):
    print('Qual foi a nota do(a) anluno(a) em Matemática?')
    mat = float(input())
    if (mat > 7):
        print('Qual foi a classificação de poder do(a) aluno(a)?')
        poder = int(input())
        if (poder == 10):
            print('Ômega')
        else:
            print('O tipo de poder do(a) aluno(a) é Telepatia? \n1. Sim \n2. Não')
            telepatia = int(input())
            if (telepatia == 1):
                media = (port + mat + (poder * 2)) / 3
                print('A média do aluno é: %.2f' % (media))
            else:
                media = (port + mat + poder) / 3
                print('A média do aluno é: %.2f' % (media))
    else:
        print('O(A) aluno(a) foi reprovado na segunda etapa')
else:
    print('O(a) aluno(a) foi reprovado na primeira etapa')