import math

angulo = float(input('Digite o ângulo que você deseja: '))
radianos = math.radians(angulo)
print(f'O ângulo de {angulo} tem o seno de {math.sin(radianos):.2f}')
print(f'O ângulo de {angulo} tem o cosseno de {math.cos(radianos):.2f}')
print(f'O ângulo de {angulo} tem o tangente {math.tan(radianos):.2f}')