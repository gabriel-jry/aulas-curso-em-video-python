frase = str(input('Digite uma frase: ')).lower().strip()
print(f'A letra A apareceu na posição {frase.index('a')+1}')
print(f'A última letra A apareceu na posição {frase.rfind('a')}')