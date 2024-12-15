dados=list()
cadastros=list()
dlev=list()
dpes=list()
lev=list()
pes=list()
som=0
while True:
    nome=str(input('NOME: ')).upper().strip()
    dados.append(nome)
    massa=float(input('MASSA(Kg): '))
    som+=massa
    dados.append(massa)
    cadastros.append(dados[:])
    dados.clear()
    med=som/len(cadastros)
    if massa>=med:
        dpes.append(massa)
        dpes.append(nome)
        pes.append(dpes[:])
    if massa<med:
        dlev.append(massa)
        dlev.append(nome)
        lev.append(dlev[:])
    dpes.clear()
    dlev.clear()
    op = str(input('[ENTER] para CONTINUAR ou [X] para ENCERRAR: ')).strip().upper()
    if op=='X':
        break
print('\n')
print('='*200)
print(f'NÚMERO DE CADASTRADOS: {len(cadastros)}')
print('='*200)
print('LISTA DOS CADASTRADOS')
print('='*200)
for i,c in enumerate(cadastros):
    print(f'{i+1}. {c[0]} - {c[1]}')
    print('-'*200)
print('='*200)
print(f'PESO MÉDIO: {med:.2f}')
print('='*200)
print('LISTA DE PESOS LEVES: ')
print('='*200)
for k,l in enumerate(lev):
    print(f'{k+1}. {l[1]} - {l[0]}')
    print('-' * 200)
print('='*200)
print('LISTA DE PESOS PESADOS: ')
print('='*200)
for q,p in enumerate(pes):
    print(f'{q+1}. {p[1]} - {p[0]}')
    print('-' * 200)