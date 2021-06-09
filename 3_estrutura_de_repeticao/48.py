"""
48. Faça um programa que peça um numero inteiro positivo
e em seguida mostre este numero invertido.
Exemplo:

12376489
=> 98467321
"""

n = int(input('Informe um número inteiro positivo: '))

# Forma com função .join e reversed
num_str = str(n)
print(''.join(reversed(num_str)))

# Forma com interação de lista na string
num_str2 = str(n)[::-1]
print(num_str2)
