soma = 0
cont = 0
for c in range(1, 7):
  número = int(input(f'Digite o valor {c}: '))
  if número % 2 == 0:
    soma += número
    cont += 1
print(f'Você informou {cont} números pares e a soma deles é {soma}.')