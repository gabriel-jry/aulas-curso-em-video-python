from time import sleep
lista = []
aluno = []
notas = []
qt = 0
while True:
    nome = str(input('Nome: '))
    n1 = float(input('1ª Nota: '))
    n2 = float(input('2ª Nota: '))
    lista.append(nome)
    notas.append(n1)
    notas.append(n2)
    media = (n1 + n2) / 2
    lista.append(media)
    lista.append(notas[:])
    notas.clear()
    qt += 1
    sn = str(input('Quer continuar? [S/N] '))
    if sn in 'Nn':
        break
print('-=' * 30)
print('-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
v = 0
for p in range(1, qt+1):
    print(p, end='')
    print('     {:10}   '.format(lista[v]), end='')
    print(f'{lista[v+1]:.1f}')
    v += 3
print('-' * 70)
print('{:70}'.format('DETALHAR NOTAS DE ALUNO'))
print('*digite o nome para ver as notas e "fim" para finalizar o programa*')
print('-' * 70)
while True:
    opção = str(input(('Aluno: ')))
    if opção in lista:
        quem = lista.index(opção)
        print('-' * 30)
        print(f'Notas de {lista[quem]} são {lista[quem + 2]}')
        print('-' * 30)
    elif (opção == 'fim') or (opção == 'FIM') or (opção == 'Fim'):
        print('ENCERRANDO...')
        sleep(1)
        break
    else:
        print('Aluno não encontrado na lista. Tente novamente.')
print('-=' * 30)
print('Obrigado.')
print('<<< Programa encerrado. >>>')