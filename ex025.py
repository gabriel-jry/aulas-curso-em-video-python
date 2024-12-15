nome = str(input('Qual é o seu nome completo? ')).lower().strip()
print('Seu nome tem silva?', end=' ')
if 'silva' in nome:
    print('True')
else:
    print('False')