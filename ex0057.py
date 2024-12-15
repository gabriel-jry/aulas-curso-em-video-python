s = str(input('Por favor, digite o sexo (M ou F): ')).upper().strip()[0]
while s != 'F' and s != 'M':
    s = str(input('Dados inválidos. Por favor, digite o sexo (M ou F): ')
            ).upper().strip()[0]
if s == 'F':
    print('Sexo Feminino cadastrado.')
if s == 'M':
    print('Sexo Masculino cadastrado.')