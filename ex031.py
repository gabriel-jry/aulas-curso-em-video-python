km = float(input('Qual a distância da sua viagem? '))
print(f'O valor será R${km*0.5}' if km < 200 else f'O valor será R${km*0.45}')