from math import sqrt

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = sqrt(cateto_adjacente*cateto_adjacente + cateto_oposto*cateto_oposto)
print(f'A hipotenusa seria {hipotenusa:.2f}')