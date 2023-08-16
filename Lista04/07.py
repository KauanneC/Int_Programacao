aluno = 0

while aluno < 20:
    print('\nInforme a média do aluno:')
    media = float(input())
    if (media >= 7):
        print('Aluno Aprovado')
    else:
        print('Aluno Reprovado')
    aluno += 1