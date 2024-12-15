valor = int(input('Informe um número: '))

unidade = valor % 10
dezena = valor // 10 % 10
centena = valor // 100 % 10
milha = valor // 1000  % 10

for k, v in {'Unidade':unidade, 'Dezena':dezena, 'Centena':centena, 'Milhar':milha}.items():
    if v != 0:
        print(f'{k}: {v}')