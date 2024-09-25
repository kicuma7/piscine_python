from random import randint, choice

nome = []
for i in range(0, 4):
    nome.append(input(f'Digite o {i + 1}º nome: '))
nome_escolhido = choice(nome)
print(f'O nome sorteado foi {nome_escolhido}')