print('================== Posso Votar? ==================')
ano = int(input('Ano de nascimento: '))
def voto(ano):
    """
    ---> Valida a idade para voto opcinal, obrigatório ou não vota.
         Também verifica a alfabetização do eleitor, caso seja analfabeto, mas 
         esteja em idade de votar, o voto é opcional.
         Bloco while com o 'analf' valida se é analfabeto ou não.
         Demais condicionais validam a idade, sendo o eleitor alfabetizado:
         - 'if idade < 16' Menor de 16 anos não vota.
         - 'elif 16 <= idade < 18' Entre 16 e 18, voto opcional.
         - 'elif 18 <= idade <= 69' Entre 18 e 69, voto obrigatório.
         - 'elif idade >= 70' 70 anos em diante, voto opcional.
    """
    while True:
        analf = str(input('É analfabeto? [s/n]: ')).lower().split()[0]
        if analf in 'Ss':
            break
        elif analf in 'Nn':
            break
        elif analf != 's' or 'n':
            print('Responda sim[s] ou não[n].')
    if analf == 's':
        print('-' * 50)
        print('Voto Opcional!')
    elif analf == 'n':
        from datetime import datetime
        idade = datetime.now().year - ano
        print('-' * 50)
        print(f'Você nasceu em {ano} e tem agora {idade} anos de idade.')
        if idade < 16:
            print(f'Com {idade} anos de idade: \033[33mNão Vota!\033[m')
        elif 16 <= idade < 18:
            print('Não é analfabeto.', end='')
            print('\033[33m * Voto Opcional! * \033[m')
        elif 18 <= idade <= 69:
            print('Não é analfabeto.', end='')
            print('\033[33m * Voto Obrigatório! * \033[m')
        elif idade >= 70:
            print('Não é analfabeto.', end='')
            print('\033[33m * Voto opcional. * \033[m')    
            
#Programa Principal
voto(ano)
print('-' * 50)
manual = str(input('Deseja ver docstring? [s/n]: ')).lower().split()[0]
if manual in 'Ss':
    help(voto)
else:
    print('-- PROGRAMA ENCERRADO --')
print('=' * 50)