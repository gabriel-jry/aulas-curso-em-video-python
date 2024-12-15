print('{:=^30}'.format('Gerador de P.A'))
primeiro_termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
ultimo_termo = int(input('Diga qual termo você deseja: '))
contar = 0
while contar < ultimo_termo:
    contar += 1
    print(' {} '.format(primeiro_termo+razão), end='')
    if contar <= ultimo_termo - 1:
        print(' -> ', end='')
    elif contar >= ultimo_termo - 1:
        print(' = FIM ')
    primeiro_termo += razão