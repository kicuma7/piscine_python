import random

nome = []
for x in range(0, 4):
    nome.append(input(f'Digite o {x + 1}º nome: '))
random.shuffle(nome)
print('A lista de apresentacao do trabalho foi sorteada da seguinte forma: ')
print(f'{nome}')