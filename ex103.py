def ficha():
    nome = input('Digite o nome: ').strip()
    gols = input('Quantos gols foram feitos: ').strip()
    if gols == '':
        gols = int(0)
    if nome == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {gols} gols na partida.'


print(ficha())
print()