from random import randint
v=0
while True:
    computador=randint(0,10)
    jogador=int(input("Digite um numero: "))
    total = computador + jogador
    esc=" "
    while esc not in "PI":
        esc=str(input("Voce quer P/I? ")).upper()
    if esc=="P" and total%2==0:
        print("Voce venceu")
        print(f"Voce jogou {jogador} e o computador {computador} a soma é {total}")
        v=v+1
    elif esc=="I" and total%2==1:
        print("Voce venceu")
        print(f"Voce jogou {jogador} e o computador {computador} a soma é {total}")
        v=v+1
    else:
        print("Voce Perdeu")
        print(f"Voce jogou {jogador} e o computador {computador} a soma é {total}")
        break
print(f"Voce venceu com {v} vitorias")