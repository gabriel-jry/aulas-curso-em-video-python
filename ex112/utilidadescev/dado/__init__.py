def resumo(num=0, aumento=0, diminuicao=0):
    resultado = f"""
Preço analisado: {moeda(num)}
Dobro do preço: {dobro(num, True)}
Metade do preço: {metade(num, True)}
{aumento}% de aumento: {aumentar(num, aumento, True)}
{diminuicao}% de redução: {diminuir(num, diminuicao, True)}
    """
    return resultado


def moeda(num=0, moeda="R$"):
    return f"{moeda} {num:.2f}".replace(".", ",")


def metade(num=0, is_formatted=False):
    resultado = num / 2
    return moeda(resultado) if is_formatted else resultado


def dobro(num=0, is_formatted=False):
    resultado = num * 2
    return moeda(resultado) if is_formatted else resultado


def diminuir(num=0, taxa=0, is_formatted=False):
    resultado = num - (taxa * num / 100)
    return moeda(resultado) if is_formatted else resultado


def aumentar(num=0, taxa=0, is_formatted=False):
    resultado = num + (taxa * num / 100)
    return moeda(resultado) if is_formatted else resultado

def leiaDinheiro(msg):
    while True:
        res = str(input(msg).replace(',','.'))
        if res.replace('.','').isnumeric():
            break
        else:
            print(f'\033[0;31mERRO: "{res}" é um preço inválido!\033[m')
    return float(res)