def dobro(preco):
    global dobro
    moeda(preco)
    dobro = precoconv*2
    return str(dobro).replace('.', ',')
def metade(preco):
    moeda(preco)
    metade = precoconv*0.5
    return str(metade).replace('.', ',')
def aumentar(preco):
    moeda(preco)
    aumento = precoconv*1.10
    return str(aumento).replace('.', ',')
def diminuir(preco):
    moeda(preco)
    desconto = precoconv*0.90
    return str(desconto).replace('.', ',')

def moeda(preco):
    global precoconv
    preco2 = preco.replace(',', '.')
    precoconv = float(preco2)



preco = str(input('Digite o preco: R$ '))
metade = metade(preco)
dobro = dobro(preco)
aumento = aumentar(preco)
desconto = diminuir(preco)
print(f'A metade de {preco} é {metade}')
print(f'O dobro de {preco} é {dobro}')
print(f'Preço aumentou 10%, agora custa {aumento}')
print(f'Ofereço um desconto de 10%, o preço passa para {desconto}')