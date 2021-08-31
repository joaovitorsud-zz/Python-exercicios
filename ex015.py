dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos km rodados?'))
valor_por_dia = dias * 60
valor_por_km = km * 0.15
total = valor_por_dia + valor_por_km
print('O total a pagar é de R${}'.format(total))
