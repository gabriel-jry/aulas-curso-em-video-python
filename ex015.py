dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
print(f'O total a pagar é: R$ {dias*60+km*0.15:.2f}')