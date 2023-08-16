import random

flash = 300.000
primeiro_lugar = 0
segundo_lugar = 0
terceiro_lugar = 0
nome_primeiro = ''
nome_segundo = ''
nome_terceiro = ''

jesseQuick = random.randint(1,12)
barryAllen = random.randint(1,12)
wallyWest = random.randint(1,12)
drWells = random.randint(1,12)
jayGarrick = random.randint(1,12)
maxMercury = random.randint(1,12)

if (jesseQuick > primeiro_lugar):
    primeiro_lugar = jesseQuick
    nome_primeiro = 'Jesse Quick'

if (barryAllen > primeiro_lugar):
    primeiro_lugar = barryAllen
    nome_primeiro = 'Barry Allen'
    segundo_lugar = jesseQuick
    nome_segundo = 'Jesse Quick'
else:
    segundo_lugar = barryAllen
    nome_segundo = 'Barry Allen'

if (wallyWest > primeiro_lugar):
    terceiro_lugar = segundo_lugar
    nome_terceiro = nome_segundo
    segundo_lugar = primeiro_lugar
    nome_segundo = nome_primeiro
    primeiro_lugar = wallyWest
    nome_primeiro = 'Wally West'
elif (wallyWest > segundo_lugar):
    terceiro_lugar = segundo_lugar
    nome_terceiro = nome_segundo
    segundo_lugar = wallyWest
    nome_segundo = 'Wally West'
else:
    terceiro_lugar = wallyWest
    nome_terceiro = 'Wally West'

if (drWells > primeiro_lugar):
    terceiro_lugar = segundo_lugar
    nome_terceiro = nome_segundo
    segundo_lugar = primeiro_lugar
    nome_segundo = nome_primeiro
    primeiro_lugar = drWells
    nome_primeiro = 'Dr. Wells' 
elif (drWells > segundo_lugar):
    terceiro_lugar = segundo_lugar
    nome_terceiro = nome_segundo
    segundo_lugar = drWells
    nome_segundo = 'Dr. Wells'
else:
    terceiro_lugar = drWells
    nome_terceiro = 'Dr. Wells'

if (jayGarrick > primeiro_lugar):
    terceiro_lugar = segundo_lugar
    nome_terceiro = nome_segundo
    segundo_lugar = primeiro_lugar
    nome_segundo = nome_primeiro
    primeiro_lugar = jayGarrick
    nome_primeiro = 'Jay Garrick'
elif (jayGarrick > segundo_lugar):
    terceiro_lugar = segundo_lugar
    nome_terceiro = nome_segundo
    segundo_lugar = jayGarrick
    nome_segundo = 'Jay Garrick'
else:
    terceiro_lugar = jayGarrick
    nome_terceiro = 'Jay Garrick'

if (maxMercury > primeiro_lugar):
    terceiro_lugar = segundo_lugar
    nome_terceiro = nome_segundo
    segundo_lugar = primeiro_lugar
    nome_segundo = nome_primeiro
    primeiro_lugar = maxMercury
    nome_primeiro = 'Max Mercury'
elif (maxMercury > segundo_lugar):
    terceiro_lugar = segundo_lugar
    nome_terceiro = nome_segundo
    segundo_lugar = maxMercury
    nome_segundo = 'Max Mercury'
else:
    terceiro_lugar = maxMercury
    nome_terceiro = 'Max Mercury'

print('Jesse Quick:', (jesseQuick * flash), 'Km/s')
print('Barry Allen:', (barryAllen * flash), 'Km/s')
print('Wally West:', (wallyWest * flash), 'Km/s')
print('Dr. Wells:', (drWells * flash), 'Km/s')
print('Jay Garrik:', (jayGarrick * flash), 'Km/s')
print('Max Mercury:', (maxMercury * flash), 'Km/s')

print('Primeiro Lugar:', nome_primeiro, '\nSegundo Lugar:', nome_segundo, "\nTerceiro Lugar:", nome_terceiro)