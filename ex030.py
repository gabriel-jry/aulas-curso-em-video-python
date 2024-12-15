número = int(input('\033[35mMe diga um número qualquer: \033[m'))
print(f'O número {número} é IMPAR' if número % 2 == 1 else f'O número {número} é PAR')