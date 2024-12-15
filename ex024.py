cidade = str(input('Em que cidade você nasceu? ')).strip().lower()

if cidade.split()[0] == 'santo':
    print('True')
else:
    print('False')