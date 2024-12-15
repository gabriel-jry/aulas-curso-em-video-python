valor = float(input('Digite o valor atual: '))
print(f'O novo salário será de R${valor*10/100+valor}' if valor >= 1250 else f'O novo salário será de R${valor*15/100+valor}')