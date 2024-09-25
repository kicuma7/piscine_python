dias = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos KM rodou: '))
preco = (km * 0.15) + (dias * 60)
print(f'O valor a pagar pelo aluguel do carro sera de {preco:.2f}')