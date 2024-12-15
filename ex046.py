from time import sleep
color = int(input('''\033[1;37m> Escolha uma das cores abaixo:
\033[31m[ 0 ] Vermelho
\033[34m[ 1 ] Azul
\033[35m[ 2 ] Rosa
\033[32m[ 3 ] Verde
\033[33m[ 4 ] Amarelo
\033[36m... \033[m'''))
print('\n' * 5)
print('\033[1;36m=-->-\033[m' * 20)

for c in range(10, -1, -1):
    print(c)
    sleep(1)
if color == 0:
    print('\033[1;31m BOOM!')
    print('Feliz Ano Novo :)')
elif color == 1:
    print('\033[1;34m BOOM!')
    print('Feliz Ano Novo :)')
elif color == 2:
    print('\033[1;35m BOOM!')
    print('Feliz Ano Novo :)')
elif color == 3:
    print('\033[1;32m BOOM!')
    print('Feliz Ano Novo :)')
elif color == 4:
    print('\033[1;33m BOOM!')
    print('Feliz Ano Novo :)')
elif color == 100:
    print('\033[1;36mB\033[35mO\033[34mO\033[33mM\033[32m!\033[m')
    print('\033[31mFeliz Ano Novo :)')