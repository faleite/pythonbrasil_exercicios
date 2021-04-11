"""
21. Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque
e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
    a. Exemplo 1: Para sacar a quantia de 256 reais,
o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

print('Valor mínimo para saque: R$ 10,00.')
print('Valor máximo para saque: R$ 600,00.')
saque = int(input('Insira o valor do saque: '))

while saque < 10 or saque > 600:
    print('Valor inválido.')
    saque = int(input('Tente novamente: '))
else:
    nota = saque // 100
    saque = saque - (nota * 100)
    print(f'{nota} nota(s) de R$ 100,00')

    nota = saque // 50
    saque = saque - (nota * 50)
    print(f'{nota} nota(s) de R$ 50,00')

    nota = saque // 10
    saque = saque - (nota * 10)
    print(f'{nota} nota(s) de R$ 10,00')

    nota = saque // 5
    saque = saque - (nota * 5)
    print(f'{nota} nota(s) de R$ 5,00')

    nota = saque // 1
    print(f'{nota} nota(s) de R$ 1,00')
