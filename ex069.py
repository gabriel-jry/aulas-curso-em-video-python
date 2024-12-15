ps = 0
ho = 0
mu = 0
total = 0
resposta = 's'
while resposta not in 'Nn':
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    if idade > 18:
        ps += 1
    if sexo.upper() == 'M':
        ho += 1
    if sexo.upper() == 'F' and idade < 20:
        mu += 1
    total += 1
    resposta = str(input('Quer continuar? '))
print(f'No total {ps} pessoas adultas foram registradas. Foram um total de {ho} homens registrados, e {mu} são mulheres com menos de 20 anos registradas.')