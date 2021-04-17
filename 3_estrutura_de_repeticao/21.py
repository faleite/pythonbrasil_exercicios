"""
21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

num = int(input('Insira um número: '))

mult = 0

for i in range(2, num):
    if num % i == 0:
        mult += 1
if mult == 0:
    print(f'{num} é um número primo.')
else:
    print(f'{num} não é um número primo.')

""" Fazer com While """
# i = 0
# mult = 0
#
# while i < num:
#     i += 1
#     if num % i == 0:
#         mult += 1
#
# if mult == 2:
#     print(f'{num} é um número primo.')
# else:
#     print(f'{num} não é um número primo.')
