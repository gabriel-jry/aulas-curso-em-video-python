casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
tempo = float(input('Em quantos anos você quer pagar? '))

if casa / (tempo * 12) > salario * 30 / 100:
    print(f'Emprestimo negado! prestações de R${casa/(tempo*12):.2f}')
else:
    print(f'Emprestimo aprovado! prestações de R${casa/(tempo*12):.2f}')