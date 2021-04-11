"""
24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
a. par ou ímpar;
b. positivo ou negativo;
c. inteiro ou decimal.
"""

num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))
operacao = int(input('Insira a operação: 1-Adição, 2-Subtração, 3-Multiplicação e 4-Divisão: '))

print('O número é:')

if operacao == 1:
    resultado = num1 + num2
elif operacao == 2:
    resultado = num1 - num2
elif operacao == 3:
    resultado = num1 * num2
elif operacao == 4:
    resultado = num1 / num2

if resultado % 2 == 0:
    print('a. Par')
else:
    print('a. Impar')

if resultado < 0:
    print('b. Negativo')
else:
    print('b. Positivo')

if resultado == round(resultado):
    print('c. Inteiro')
else:
    print('c. Decimal')
