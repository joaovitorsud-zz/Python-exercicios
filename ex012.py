valor = float(input('digite o preço'))
desconto = float(input('digite o desconto em porcentagem'))
desconto1 = (valor * desconto)/100
print('o desconto foi de {}'.format(desconto1))
print('o preço final é de {}'.format(valor-desconto1))
