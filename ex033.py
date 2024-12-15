n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

for e, valor in enumerate([n1, n2, n3]):
    if e == 0:
        M = valor
        m = valor
    if valor > M:
        M = valor
    elif valor < m:
        m = valor

print(f'Maior: {M} menor: {m}')