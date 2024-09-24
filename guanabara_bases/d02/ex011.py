height = float(input('Type the wall height: '))
width = float(input('Type the wall width: '))
area = width * height
print(f'The Area is {(area):.2f} m2', end=' ')
print(f'To fill all the wall you will need {(area / 2):.2f} liters of ink')