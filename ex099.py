def imprimelinha():
    print('-' * 30)


def maior():
    imprimelinha()
    cont = 0
    numeros = []
    while True:
        num = int(input('Digite um valor: '))
        cont += 1
        numeros.append(num)
        resp = str(input('Continuar S/N? ')).strip().upper()[0]
        while resp not in 'SN':
            resp = str(input('Continuar S/N? ')).strip().upper()[0]
        if resp == 'N':
            break
    print('Analisando os valores informados...')
    print(f'Foram informados {cont} valores:', end=' ')
    for v in numeros:
        print(f'{v}', end=' ')
    print(f'\nO maior valor informado foi {max(numeros)}')

# Programa Principal
maior()