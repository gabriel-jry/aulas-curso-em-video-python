print('-=-'*20)
print('Analisador de triângulos')
print('-=-'*20)

p1 = float(input('Primeiro segmento: '))
p2 = float(input('Segundo segmento: '))
p3 = float(input('Terceiro segmento: '))

if (p1 + p2) > p3 and (p2 + p3) > p1 and (p1 + p3) > p2:
    print('Pode formar um triangulo!')
else:
    print('Não pode formar um triangulo!')