""" 17. Faça um Programa que peça um número correspondente
a um determinado ano e em seguida informe se este ano é ou não bissexto.
"""

ano = int(input(f'Insira o ano: '))

if ano % 4 == 0 and ano % 100 != 0:
    print(f'{ano} é um ano Bissexto')
elif ano % 4 != 0 and ano % 400 != 0:
    print(f'{ano} não é um ano Bissexto')
elif ano % 4 != 0 and ano % 400 == 0:
    print(f'{ano} é um ano Bissexto')
