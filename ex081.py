from time import sleep

def line2():
	print("=" *55)
def line():
	print("-" *55)
	
lista = []

print(f"{'[ ANALISANDO VALORES NUMA LISTA ]': ^53}")
line2()
while True:
	lista.append(int(input("Digite um valor = ")))
	option = " "
	while option not in "SsNn":
		option = input("Continuar?[S/N] = ").upper()
	if option == "N":
		break
	line()

print("Analisando...")
sleep(1.5)

line()
print(f"Sua lista = {lista}")
sleep(1)

print(f"Tamanho da lista = {len(lista)}") #[a]
sleep(1)

print(f"Ordem decrescente = {sorted(lista, reverse = True)}") #[b]
sleep(1)

if 5 in lista: #[c]
	print("O n°5 está na lista!")
else:
	print("O n°5 não está na lista!")
sleep(1)
line()