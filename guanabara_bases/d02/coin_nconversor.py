from requests import get

orig = 'USD'
dest = 'AOA'
link = f'https://economia.awesomeapi.com.br/last/{orig}-{dest}'
req = get(link)
price = float(req.json()[f'{orig}{dest}']['bid'])
money = float(input(f'Type how much {dest} you have: '))
print(f'With {money:.1f} {dest} you can buy {money / price:.2f} {orig}')