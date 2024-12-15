def metade(valor=0, formato=False):
    res = int(valor) / 2
    if formato:
        return moeda(res)
    else:
        return res

def dobro(valor=0, formato=False):
    res = valor * 2
    if formato:
        return moeda(res)
    else:
        return res

def aumentar(valor=0, taxa=0, formato=False):
    res = valor + (valor * taxa / 100)
    if formato:
        return moeda(res)
    else:
        return res

def diminuir(valor, taxa, formato=False):
    res = valor - (valor * taxa / 100)
    if formato:
        return moeda(res)
    else:
        return res

def moeda(valor=0, símbolo='R$'):
    return f'{símbolo}{valor:.2f}'.replace('.', ',')

def resumo(valor, aumento, redução):
    tabela = dict()
    tabela['Preço analisado:'] = moeda(valor)
    tabela['Dobro do preço:'] = dobro(valor, True)
    tabela['Metade do preço:'] = metade(valor, True)
    tabela[f'{aumento}% de aumento:'] = aumentar(valor, aumento, True)
    tabela[f'{redução}% de redução:'] = diminuir(valor, redução, True)
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    for k, v in tabela.items():
        print(f'{k: <20}{v}')
    print('-' * 30)

número = float(input('Digite o preço: R$'))
resumo(número, 20, 12)