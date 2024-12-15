from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano do seu nascimento? '))
idade = atual - nasc
print(f'\033[34mSua idade é de {idade} ano(s).\033[m')
if idade <= 9:
    print('\033[35mCategoria: MIRIM.\033[m')
elif idade > 9 and idade <= 14:
    print('\033[36mCategoria: INFANTIL.\033[m')
elif idade > 14 and idade <= 19:
    print('\033[33mCategoria: JÚNIOR.\033[m')
elif idade > 19 and idade <= 25:
    print('\033[31mCategoria: SÊNIOR.\033[m')
else:
    print('\033[37mCategoria: MASTER\033[m')