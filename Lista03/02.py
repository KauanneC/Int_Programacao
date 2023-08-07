tempo = 50

print('Chico calçou a botinha? \n1. Sim \n2. Não')
botinha = int(input()) #40min

if (botinha == 1):
    tempo = 40

print('Chico foi montado no Teobaldo? \n1. Sim \n2. Não')
teobaldo = int(input()) # -30min

if (teobaldo == 1):
    tempo -= 30  

print('Está um dia quente? \n1. Sim \n2. Não')
dia = int(input()) # +40min

if (dia == 1):
    tempo += 40

print('Chico saiu sem café da manhã? \n1. Sim \n2. Não')
cafe = int(input()) # +20min

if (cafe == 1):
    tempo += 20

print('Chico encontrou Rosinha? \n1. Sim \n2. Não')
rosinha = int(input())

if (rosinha == 1):
    print('Quantas pitalinas Chico trocou com Rosinha?')
    pitalina = int(input()) # +10min p/ cada
    
    tempo = pitalina * 10

print('Chico foi surpreendido pela onça? \n1. Sim \n2. Não')
onca = int(input()) # 30min

if (onca == 1):
    tempo -= 30

print('Tempo gasto: ' + str(tempo) + 'min')