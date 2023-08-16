jogo1 = 0
jogo2 = 0
jogo3 = 0
jogo4 = 0
jogo5 = 0
jogo6 = 0
jogo7 = 0
jogo8 = 0
jogo9 = 0
jogo10 = 0
jogo11 = 0
jogo12 = 0

n_jogo1 = 'Metal Gear Solid'
n_jogo2 = 'Driver'
n_jogo3 = 'Crash Bandicoot'
n_jogo4 = 'Warped'
n_jogo5 = 'Tekken 3'
n_jogo6 = 'Cortex Strikes Back'
n_jogo7 = 'Final Fantasy VIII'
n_jogo8 = 'Gran Turismo 2'
n_jogo9 = 'Gran Turismo'

i = 0

while i < 35:
    print('Qual seu jogo preferido? \n1. Metal Gear Solid \n2. Driver \n3. Crash Bandicoot \n4. Warped \n5. Tekken 3 \n6. Cortex Strikes Back \n7. Final Fantasy VIII \n8. Gran Turismo 2 \n9.Gran Turismo')
    opcao = int(input())

    if (opcao == 1):
        jogo1 += 1
    elif (opcao == 2):
        jogo2 += 1
    elif (opcao == 3):
        jogo3 += 1
    elif (opcao == 4):
        jogo4 += 1
    elif (opcao == 5):
        jogo5 += 1
    elif (opcao == 6):
        jogo6 += 1
    elif (opcao == 7):
        jogo7 += 1
    elif (opcao == 8):
        jogo8 += 1
    else: 
        jogo9 += 1

    i += 1

if (jogo1 > jogo2) and (jogo1 > jogo3) and (jogo1 > jogo4) and (jogo1 > jogo5) and (jogo1 > jogo6) and (jogo1 > jogo7) and (jogo1 > jogo8) and (jogo1 > jogo9):
    print('Jogo preferido da turma:', n_jogo1)

elif (jogo2 > jogo1) and (jogo2 > jogo3) and (jogo2 > jogo4) and (jogo2 > jogo5) and (jogo2 > jogo6) and (jogo2 > jogo7) and (jogo2 > jogo8) and (jogo2 > jogo9):
    print('Jogo preferido da turma:', n_jogo2)

elif (jogo3 > jogo1) and (jogo3 > jogo2) and (jogo3 > jogo4) and (jogo3 > jogo5) and (jogo3 > jogo6) and (jogo3 > jogo7) and (jogo3 > jogo8) and (jogo3 > jogo9):
    print('Jogo preferido da turma:', n_jogo3)

elif (jogo4 > jogo1) and (jogo4 > jogo2) and (jogo4 > jogo3) and (jogo4 > jogo5) and (jogo4 > jogo6) and (jogo4 > jogo7) and (jogo4 > jogo8) and (jogo4 > jogo9):
    print('Jogo preferido da turma:', n_jogo4)

elif (jogo5 > jogo1) and (jogo5 > jogo2) and (jogo5 > jogo3) and (jogo5 > jogo4) and (jogo5 > jogo6) and (jogo5 > jogo7) and (jogo5 > jogo8) and (jogo5 > jogo9):
    print('Jogo preferido da turma:', n_jogo5)

elif (jogo6 > jogo1) and (jogo6 > jogo2) and (jogo6 > jogo3) and (jogo6 > jogo4) and (jogo6 > jogo5) and (jogo6 > jogo7) and (jogo6 > jogo8) and (jogo6 > jogo9):
    print('Jogo preferido da turma:', n_jogo6)

elif (jogo7 > jogo1) and (jogo7 > jogo2) and (jogo7 > jogo3) and (jogo7 > jogo4) and (jogo7 > jogo5) and (jogo7 > jogo6) and (jogo7 > jogo8) and (jogo7 > jogo9):
    print('Jogo preferido da turma:', n_jogo7)

elif (jogo8 > jogo1) and (jogo8 > jogo2) and (jogo8 > jogo3) and (jogo8 > jogo4) and (jogo8 > jogo5) and (jogo8 > jogo6) and (jogo8 > jogo7) and (jogo8 > jogo9):
    print('Jogo preferido da turma:', n_jogo8)

else:
    print('Jogo preferido da turma:', n_jogo9)