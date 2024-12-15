n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('A média do aluno é {:.1f}. \nREPROVADO.'.format(media))
elif media >= 7:
    print('A média do aluno é {:.1f}. \nAPROVADO.'.format(media))
else:
    print('A média do aluno é {:.1f}. \nRECUPERAÇÃO.'.format(media))