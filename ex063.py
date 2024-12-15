n = int(input('POSIÇÃO FINAL : '))
termo1 = 0
termo2 = 1
contador = 3
print('{} -> {}'.format(termo1,termo2),end='')
while contador <= n:
    termo3 = termo1 + termo2
    print(' -> {}'.format(termo3),end='')
    termo1 = termo2
    termo2 = termo3
    contador+=1
print(' -> FIM')

MINHA SOLUÇÃO(COLORIDA)

n = int(input('\033[7;31;40mPOSIÇÃO FINAL :\033[m '))
termo1 = 0
termo2 = 1
contador = 3
print('\033[1m{}\033[m \033[1;36m->\033[m \033[1m{}\033[1m'.format(termo1,termo2),end='')
while contador <= n:
    termo3 = termo1 + termo2
    print(' \033[1;36m->\033[m \033[1m{}\033[m'.format(termo3),end='')
    termo1 = termo2
    termo2 = termo3
    contador+=1
print(' \033[1;36m->\033[m \033[1;31m[ F I M ]\033[m'