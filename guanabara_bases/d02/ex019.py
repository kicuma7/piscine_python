from math import radians, sin, cos, tan

angulo = float(input('Digite o angulo que deseja calcular: '))
angulo = radians(angulo);
seno = sin(angulo)
coseno = cos(angulo)
tangente = tan(angulo)
print(f'Seno: {seno:.2f}')
print(f'Coseno: {coseno:.2f}')
print(f'Tangente: {tangente:.2f}')