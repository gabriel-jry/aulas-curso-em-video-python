from random import randint
from time import sleep

print('\033[1;33m-=-\033[m'*12)
print(f'\033[1;33m------\033[m \033[4;31mPALPITES PARA MEGA SENA\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*12, '\n')
num = randint(1, 60)
lista = []
listatemp = []
cont = 0
c = 0
jogos = int(input('Digite a quantidade de jogos que deseja fazer: '))
while c < jogos:
    while True:
        num = randint(1, 60)
        if num not in listatemp:
            listatemp.append(num)
            #print(lista)
            cont += 1
            if cont >= 6:
                c += 1
                listatemp.sort()
                break
    cont = 0
    lista.append(listatemp[:])
    listatemp.clear()
for i, l in enumerate(lista):
    print(f'Palpite {i+1}: {l}')
    sleep(1)