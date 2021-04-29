"""
34. Os números primos possuem várias aplicações dentro da Computação,
por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo.
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
"""


def num_primo(*args):
    mult = 0
    for i in range(num):
        i += 1
        if num % i == 0:
            mult += 1
    if mult <= 2:
        return f'{num} é um número primo'
    else:
        return f'{num} não é um número primo'


num = int(input('Insira um número inteiro: '))
print(num_primo(num))
