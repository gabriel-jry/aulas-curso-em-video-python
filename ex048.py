print("Aviso! todos os valores somados serao impares e multiplos de 3")
n1 = int(input("digite qual o valor maximo: "))
soma = 0
vzs = 0

for c in range(0, n1, 3):
    if c % 2 == 1:
        soma = soma + c
        vzs = vzs + 1
print("A soma de todos os {} valores são de {}".format(vzs, soma))