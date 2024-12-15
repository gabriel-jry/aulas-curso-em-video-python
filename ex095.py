from time import sleep
resp = None
gols = []
dado = []
while resp != 'N':
    nome = str(input('Nome do jogador: '))
    quantidade = int(input(f'Quantidade de partidas de {nome}: '))
    for c in range(quantidade):
        gol = int(input(f'Quantidade de gols na {c + 1}º partida: '))
        gols.append(gol)
    info = {'nome': nome, 'quantidade': quantidade, 'gols': gols[:], 'soma': sum(gols)}
    dado.append(info.copy())
    info.clear()
    gols.clear()
    resp = str(input('Quer continuar [S/N]:')).upper()[0]
print('-=' * 30)
print(f'{"cod":<4}{"nome":<11}{"gols":<15} total')
print('-' * 38)
for n, i in enumerate(dado):
    print(f'{n:<4}{i["nome"]:<11} {str(i["gols"]):<18}{i["soma"]}')
print('-' * 38)
c = 1
while True:
    detalhes = int(input('De qual jogador quer ver o levantamento?(999 para parar)\n'))
    if detalhes == 999:
        print('Finalizando...')
        sleep(1)
        break
    elif detalhes <= len(dado) - 1:
        c = 0
        print(f'-- Levantamento do jogador {dado[detalhes]["nome"]}:')
        for cp in dado[detalhes]["gols"]:
            print(f' {"No":>5} jogo {c} fez {cp} gols')
            c += 1
        print(f'No total {dado[detalhes]["soma"]} gols')
    else:
        print(f'Não existe jogador com o número {detalhes} por favor digite novamente:')
print('<<< VOLTE SEMPRE >>>')