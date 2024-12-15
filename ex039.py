from datetime import date

atual = date.today().year
ano = int(input('Ano de nascimento: '))

print(f'Quem nasceu em {ano} tem {atual - ano} anos em {atual}.')
if atual - ano < 18:
    print(f'Falta {18 - (atual - ano)} para você se alistar!')
elif atual - ano == 18:
    print('Está no ano de se alistar!')
else:
    print('Está em divida com o serviço militar!')