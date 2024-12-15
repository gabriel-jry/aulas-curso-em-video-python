def PyHELP(txt=''):
    while True:
        from time import sleep
        print('\33[42m~' * 30)
        print('   SISTEMA DE AJUDA PyHELP')
        print('~' * 30)
        print('\33[m', end='')
        txt = input('Função ou Biblioteca > ').strip()
        tam = len(txt) + 36
        if txt.lower() in 'fim':
            print('\33[1;97;41m~' * 10)
            print(f" ATÉ LOGO")
            print('~' * 10)
            break
        print('\33[30;45m~' * tam)
        print(f"  Acessando o manual do comando '{txt}'")
        print('~' * tam)
        print('\33[30;107m', end='')
        sleep(1)
        help(txt)
        print('\33[m', end='')

PyHELP()