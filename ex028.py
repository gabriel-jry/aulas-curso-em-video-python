from random import randint
print('\033[33m-=-\033[m'*20)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33m-=-\033[m'*20)
numero = int(input('Em que número eu pensei? '))
v = randint(0,5)
print('\033[35mPROCESSANDO...\033[m')
if numero != v:
    print(f'\033[31mGANHEI!, Eu pensei no número {v} e não no {numero}!\033[m')
else:
    print('\033[33mPARABÉNS! Você conseguiu me vencer!\033[m')