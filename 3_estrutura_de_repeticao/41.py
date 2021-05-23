"""
41. Faça um programa que receba o valor de uma dívida
e mostre uma tabela com os seguintes dados: valor da dívida,
valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
1   0
3   10
6   15
9   20
12  25

Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""

divida = float(input('Informe o valor da dívida: '))

print()
print('Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela')

juros = 0
parcela = 1

for i in range(1, 6):
    val_juros = (divida * juros / 100)
    val_divida = divida + val_juros
    val_parcela = val_divida / parcela
    print(f'R$ {divida:.2f}      {val_juros:.2f}            {parcela}                       R$ {val_parcela:.2f}')

    if i == 1:
        parcela = 3
        juros = 10
    else:
        parcela += 3
        juros += 5

""" primeira formula"""
# for parcela in range(1, 13):
#     if parcela == 1:
#         juros = 0
#         val_parcela = divida
#         print(f'R$ {divida:.2f}      {juros}               {parcela}                       R$ {val_parcela:.2f}')
#     if parcela == 3:
#         juros = (divida * 10 / 100)
#         val_divida = divida + juros
#         val_parcela = val_divida / 3
#         print(f'R$ {val_divida:.2f}      {juros:.2f}          {parcela}                       R$ {val_parcela:.2f}')
#     if parcela == 6:
#         juros = (divida * 15 / 100)
#         val_divida = divida + juros
#         val_parcela = val_divida / 6
#         print(f'R$ {val_divida:.2f}      {juros:.2f}          {parcela}                       R$ {val_parcela:.2f}')
#     if parcela == 9:
#         juros = (divida * 20 / 100)
#         val_divida = divida + juros
#         val_parcela = val_divida / 9
#         print(f'R$ {val_divida:.2f}      {juros:.2f}          {parcela}                       R$ {val_parcela:.2f}')
#     if parcela == 12:
#         juros = (divida * 25 / 100)
#         val_divida = divida + juros
#         val_parcela = val_divida / 12
#         print(f'R$ {val_divida:.2f}      {juros:.2f}          {parcela}                      R$ {val_parcela:.2f}')
