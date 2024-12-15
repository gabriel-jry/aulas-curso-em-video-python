#importações
from datetime import date
from time import sleep

#dicionários

dados  = dict()

#configurando nome e sexo

dados['nome'] = str(input('\033[0;34m digite o seu nome:\033[m ')).strip().capitalize()
dados['sexo'] = str(input('\033[0;34m sexo [M/F]:\033[m ')).strip().upper()
sleep(0.07)
print('\033[0;36m aguardando...')
sleep(0.5)
print('\033[0;36m registrado')
print(' ')
print('\033[0;33m x-x-x-x-x-x-x' * 7)
print(' ')

#configurando data e idade

dados['idade'] = date.today().year - int(input('\033[0;34m Digite o ano da nascimento:\033[m '))
sleep(0.07)
print('\033[0;36m aguardando...')
sleep(0.5)
print('\033[0;36m registrado')
print(' ')
print('\033[0;33m x-x-x-x-x-x-x' * 7)
print(' ')

#configurando carteira de trabalho

request = str(input('\033[0;34m tem carteira de trabalho? [S/N]:\033[m ')).strip().upper()
if request in 'Ss' or request == 'SIM':
    print('\033[0;33m x-x-x-x-x-x-x' * 7)
    ctps = int(input('\033[0;34m carteira de trabalho [0 não tem]:\033[m '))
    if ctps == 0:
        while True:
            print('\033[0;31m invalido')
            rm = str(input('\033[0;34m Quer remover a carteira de trabalho? [S/N]: ')).strip().upper()
            if rm in 'Nn' or rm == 'NÃO':
                ctps = int(input('\033[0;34m carteira de trabalho [0 não tem]:\033[m '))
                if ctps != 0:
                    dados['ctps'] = ctps
                    dados['salário'] = float(input('\033[0;34m salário  da contratação: R$\033[m'))
                    dados['adc'] = int(input('\033[0;34m Ano de contratação: \033[m'))
                    del(rm, ctps, request)
                    break
            if rm in 'Ss' or rm == 'SIM':
                request = 'N'
                del(rm, ctps)
                break 
    else:
        dados['ctps'] = ctps
        dados['salário'] = float(input('\033[0;34m salário  da contratação: R$\033[m'))
        dados['adc'] = int(input('\033[0;34m Ano de contratação: \033[m'))
        #masculino
        if dados['sexo'] in 'Mm' or dados['sexo'] == 'MASCULINO':
            dados['sex'] = 'Masculino'    
            dados['idadeaposentadoria'] = dados['idade'] + (35 - (date.today().year - dados['adc']))
            dados['anoaposentadoria'] = date.today().year + (35 - (date.today().year - dados['adc']))
            dados['restocontribuição'] = 35 - (date.today().year - dados['adc'])
        #feminino
        if dados['sexo'] in 'Ff' or dados['sexo'] == 'FEMININO':
            dados['sex'] = 'Feminino'
            dados['idadeaposentadoria'] = dados['idade'] + (30 - (date.today().year - dados['adc']))
            dados['anoaposentadoria'] = date.today().year + (30 - (date.today().year - dados['adc']))
            dados['restocontribuição'] = 30 - (date.today().year - dados['adc'])
        del(ctps)
else:
    request = 'N'
sleep(0.07)
print('\033[0;36m aguardando...')
sleep(0.5)
print('\033[0;36m registrado')
print(' ')
print('\033[0;33m x-x-x-x-x-x-x' * 7)
print(' ')

#finalizando

print('\033[0;32m nome: ', dados['nome'])
print('\033[0;35m ----------------')
print('\033[0;32m idade: ', dados['idade'])
print('\033[0;35m ----------------')
print('\033[0;32m sexo: ', dados['sex'])
print('\033[0;35m ----------------')
if request != 'N': 
    print('\033[0;32m ctps da carteira de trabalho: ', dados['ctps'])
    print('ano de contratação: ', dados['adc'])
    print('salário: ', dados['salário'])
    print('idade de aposentadoria: ', dados['idadeaposentadoria'])
    print('ano de aposentadoria: ', dados['anoaposentadoria'])
    print('anos de contribuição para aposentadoria: ', dados['restocontribuição'])
else:
    print('\033[0;32m sem carteira de trabalho')
print('\033[0;35m ----------------')
sleep(0.07)
print('\033[0;36m aguardando...')
sleep(0.5)
print('\033[0;36m registrado')
print(' ')
print('\033[0;33m x-x-x-x-x-x-x' * 7)
print(' ')

#fim

print('\033[m FIM')