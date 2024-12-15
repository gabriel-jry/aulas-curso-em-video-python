from time import sleep
V = 0
H = 0
maior = 0
menor = 0
B = 'M'.upper()
R = 'F'.upper()
for c in range(1, 5):
    print('-=-'*7,'Dados da {}º pessoa'.format(c),'-=-'*7,)
    print('')
    N = str(input('Nome: ')).strip().upper()
    sleep(1)
    I = int(input('Idade: '))
    sleep(1)
    S = str(input('Sexo (M/F): ')).strip().upper()
    sleep(1)
    print('')
    V+=I
    if c == 1:
        maior = I
        menor = I
    else:
        if I > maior and S == B:
            maior = I
            D = N
        if I < menor:
            menor = I
        if I < 20 and S == R :
            H += 1
print('A média entre as idades é de {} anos.'.format(V/4))
print('O nome do homem mais velho é {} com {} anos de idade.'.format(D, maior))
print('Tem {} mulher/s que a sua idade é inferior a 20 anos.'.format(H))