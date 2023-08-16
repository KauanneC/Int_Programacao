opcao = 1
idadeMulher = 1
nomeMulher = ''
idadeHomem = 200

while opcao == 1:
    print('Informe o nome:')
    nome = input()
    
    print('Informe a idade:')
    idade = int(input())

    print('Informe o sexo. Digite: \n1. Feminino \n2. Masculino')
    sexo = int(input())

    if sexo == 1:
        if idade > idadeMulher:
            idadeMulher = idade
            nomeMulher = nome
    else:
        if idade < idadeHomem:
            idadeHomem = idade

    print('Deseja cadastrar outra pessoa? \n1. Sim \n2. Não')   # Flag de parada sempre por último
    opcao = int(input())

print('Mulher mais velha:', nomeMulher)
print('Idade do homem mais novo:', idadeHomem)