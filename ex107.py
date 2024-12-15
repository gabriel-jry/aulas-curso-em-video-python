def aumentar(a, b):
    return ((100 + b) * a) / 100


def diminuir(a, b):
    return ((100 - b) * a) / 100


def dobro(a):
    return a * 2


def metade(a):
    return a / 2



from time import sleep
# Programa Goxtoso

num = float(input('Digite o preço: R$'))
print('Analisando...')
sleep(1)
print(f'\033[0;31mO aumento de R${num:.2f} em 20% é R${aumentar(num, 20):.2f}')
sleep(0.5)
print(f'Diminuindo R${num:.2f} em 20% é R${diminuir(num, 20):.2f}')
sleep(0.5)
print(f'O dobro de R${num:.2f} é R${dobro(num):.2f}')
sleep(0.5)
print(f'E a metade de R${num:.2f} é R${metade(num):.2f}')