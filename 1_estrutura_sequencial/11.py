"""
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo.
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
"""

num1 = int(input('Insira o primeiro número inteiro: '))
num2 = int(input('Insira o segundo número inteiro: '))
num3 = float(input('Insira um número real: '))
soma_a = (num1 * 2) + (num2 / 2)
soma_b = (num1 * 3) + num3
soma_c = num3**3
print(f'O produto do dobro do primeiro com metade do segundo é: {soma_a:.0f}')
print(f'A soma do triplo do primeiro com o terceiro é: {soma_b:.0f}')
print(f'O terceiro elevado ao cubo é: {soma_c:.0f}')
