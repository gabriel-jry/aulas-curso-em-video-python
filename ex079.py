lista = []
while True:
    try:
        lista.append(int(input('Escolha um valor: ')))
        print('Valor adicionado com sucesso...')
    except ValueError:
        print('Erro ao preencher o requisito, apenas números!')
    go = ' '
    while go not in 'SN':
        go = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if go == 'N':
        break
lista.sort()
print(f'Os números listados foram: {lista}.')