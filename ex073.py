Times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Chapecoense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Vitória', 'Paraná')
alfabeto = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',\
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
print(f'Os 5 primeiros são {Times[:5]}')
print(f'Os 4 ultimos são {Times[-4:]}')
qualtime = 0
numero = 0
a = 0
for i in range(0,23):
    while numero != 20:
        time = Times[qualtime]
        if time[0] == alfabeto[a]:
            print(f'{time}',end=' ')
        numero += 1
        qualtime += 1
        if time == 'Chapecoense':
            local = numero
    numero = 0
    a += 1
    qualtime = 0
print(f'''
O Chapecoense está na {local}° posição''')