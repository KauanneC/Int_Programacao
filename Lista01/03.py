print('Informe o valor do produto')
valor = float(input())

print('Informe o número de parcelas')
parcelas = int(input())

porcent_parcelas = parcelas * 2 # Valor dado em porcentagem
total = ((valor/100) * porcent_parcelas) + valor

print('Total = ' + str(total))