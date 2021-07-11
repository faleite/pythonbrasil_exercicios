"""
49. Faça um programa que mostre os n termos da Série a seguir:

S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.
"""

n = int(input('Informe o número de termos: '))

num = razao = soma = 0
for i in range(1, n + 1):
    if razao == 0:
        razao = 1
    else:
        razao += 2
    soma += i / razao
    print(f'{i}/{razao} +', end=" ")
print('... + n/m.')
print(f'{soma:.2f}')
