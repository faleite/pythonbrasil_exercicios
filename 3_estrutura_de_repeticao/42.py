"""
42. Faça um programa que leia uma quantidade indeterminada de números positivos
e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.
"""

int_a = []
int_b = []
int_c = []
int_d = []

while True:
    num = float(input('Insira um número: '))
    if 0 <= num <= 25:
        int_a.append(num)
    elif 26 <= num <= 50:
        int_b.append(num)
    elif 51 <= num <= 75:
        int_c.append(num)
    elif 76 <= num <= 100:
        int_d.append(num)
    else:
        break

print(f'Números positivos no intervalo de [0-25]: {len(int_a)}')
print(f'Números positivos no intervalo de [26-50]: {len(int_b)}')
print(f'Números positivos no intervalo de [51-75]: {len(int_c)}')
print(f'Números positivos no intervalo de [76-100]: {len(int_d)}')

