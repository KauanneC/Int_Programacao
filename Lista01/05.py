print('Informe a temperatura em Fahrenheit')
temp_fahr = float (input())

# C = F - 32 / 1,8

celsius = ((temp_fahr - 32) / 1.8)

print('Temperatua em Celsiu: %.2F' % (celsius))