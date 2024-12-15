lstbase = list()
lstpar = list()
lstimpar = list()
while True:
    num = int(input('Digite um numero para a lista: '))
    lstbase.append(num)
    if num % 2 == 0:
        lstpar.append(num)
    else:
        lstimpar.append(num)
    op = str(input('Deseja continuar? S/N ')).strip()
    if op in 'nN':
        break
lstbase.sort()
lstpar.sort()
lstimpar.sort()
print(f'Voce digitou os valores {lstbase}')
print(f'A lista de números pares: {lstpar}')
print(f'A lista de números impares: {lstimpar}')