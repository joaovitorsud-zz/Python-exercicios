salario = float(input('Qual o salário atual?'))
aumento = float(input('Qual o valor do aumento em porcento?'))
total = (salario*aumento)/100
print('o valor final é de R${}'.format(total+salario))
