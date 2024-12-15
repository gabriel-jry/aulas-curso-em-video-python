n = int(input('Informe o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
for c in range(1,11):
    pa = n + r *c
    print(pa, end=' -> ')