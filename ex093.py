dados = dict()
gols = list()
total_gols = 0

dados['nome'] = str(input('Nome do jogador: '))
dados['partidas jogadas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, dados['partidas jogadas']):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    total_gols += gols[c]
dados['gols'] = gols.copy()
dados['total'] = total_gols
print('-'*59)
for k, v in dados.items():
    print(f'{k}: {v}')
print('-'*59)
print(dados)
print('-'*59)
print(f'O jogador {dados["nome"]} jogou {dados["partidas jogadas"]}.')
for k, v in enumerate(dados["gols"]):
    print(f'   => Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')