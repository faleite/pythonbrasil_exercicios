"""
22. Altere o programa de cálculo dos números primos, informando,
caso o número não seja primo, por quais número ele é divisível.
"""

num = int(input('Insira um número: '))

mult = 0

for i in range(num):
    i += 1
    if num % i == 0:
        mult += 1

if mult == 2:
    print(f'{num} é um número primo.')
else:
    print(f'{num} não é um número primo.')
    print('Números divisíveis:')
    for i in range(num):
        i += 1
        if num % i == 0:
            print(i, end=' ')
