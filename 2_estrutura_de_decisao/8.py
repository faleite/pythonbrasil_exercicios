""" 8. Faça um programa que pergunte o preço de três produtos
e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""

produto1 = float(input(f'Insira o primeiro preço: '))
produto2 = float(input(f'Insira o segundo preço: '))
produto3 = float(input(f'Insira o terceiro preço: '))

if produto2 > produto1 < produto3:
    print(f'O menor preço é: R$ {produto1:.2f}')
elif produto1 > produto2 < produto3:
    print(f'O menor preço é: R$ {produto2:.2f}')
else:
    print(f'O menor preço é: R$ {produto3:.2f}')

""" Outra forma: """
# produtos = [produto1, produto2, produto3]
#
# menor_preco = min(produtos)
#
# print(f'O menor preço é: R$ {menor_preco:.2f}')
