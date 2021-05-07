"""
37. Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto,
o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que
pergunte a cada um dos clientes da academia seu código, sua altura e seu peso.
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto,
do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
"""

codigo = 1
clientes = []

total_altura = 0
total_peso = 0
n_cliente = 0

while codigo:
    codigo = int(input('Informe o código do cliente, ou Digite 0 para terminar: '))
    if codigo:
        altura = float(input('Informe sua altura: '))
        peso = float(input('Informe seu peso: '))
        clientes.append({'Código': codigo, 'Altura': altura, 'Peso': peso})
        total_altura += altura
        total_peso += peso
        n_cliente += 1

mais_alto = 0
mais_baixo = 999
mais_gordo = 0
mais_magro = 999

for i in clientes:
    if i['Altura'] > mais_alto:
        cliente_alto = i['Código']
        mais_alto = i['Altura']
    if i['Altura'] < mais_baixo:
        cliente_baixo = i['Código']
        mais_baixo = i['Altura']
    if i['Peso'] > mais_gordo:
        cliente_gordo = i['Código']
        mais_gordo = i['Peso']
    if i['Peso'] < mais_magro:
        cliente_magro = i['Código']
        mais_magro = i['Peso']

print()
print('Cliente mais alto:', end=' ')
print(f'Código: {cliente_alto}, Altura: {mais_alto:.2f} m')

print('Cliente mais baixo:', end=' ')
print(f'Código: {cliente_baixo}, Altura: {mais_baixo:.2f} m')

print('Cliente mais gordo:', end=' ')
print(f'Código: {cliente_gordo}, Peso: {mais_gordo:.3f} Kg')

print('Cliente mais magro:', end=' ')
print(f'Código: {cliente_magro}, Peso: {mais_magro:.3f} Kg')

print(f'Média de altura dos clientes: {total_altura / n_cliente:.2f} m')
print(f'Média de peso dos clientes: {total_peso / n_cliente:.3f} kg')
