n = int(input('Digite um número inteiro: '))
print('''[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')

opção = str(input('Sua opção: '))
match opção:
    case '1':
        print(f'O valor {n} em binário é {bin(n)[2:]}')
    case '2':
        print(f'O valor {n} em octal é {oct(n)[2:]}')
    case '3':
        print(f'O valor {n} em hexadecimal é {hex(n)[2:]}')
    case _:
        print('ERROR, opção invalida!')