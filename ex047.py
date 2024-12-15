i = int(input('Qual será o início? '))
f = int(input('Qual será o fim? '))

for t in range(i, f+1):
    if t % 2 == 0:
        print(t, end= ' ')