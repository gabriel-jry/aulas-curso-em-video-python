from random import choice
aluno_1 = str(input('Primeiro aluno: '))
aluno_2 = str(input('Segundo aluno: '))
aluno_3 = str(input('Terceiro aluno: '))
aluno_4 = str(input('Quarto aluno: '))
alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
print(f'O aluno escolhido foi: {choice(alunos)}')