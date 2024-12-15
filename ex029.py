velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    print(f'\033[31mMULTADO! Você excedeu o limite permitido que é 80km, multade de R$ {(velocidade-80)*7}\033[m')
else:
    print('\033[33mTenha um bom dia! Dirija com segurança!\033[m')