"""
28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                     Até 5 Kg            Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne
da promoção, porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento,
valor do desconto e valor a pagar.
"""
carnes = ('File Duplo', 'Alcatra', 'Picanha')
for i, carne in enumerate(carnes, start=1):
    print(f'{i} - {carne}')
print()
tipo = int(input(f'Insira o tipo da carne: '))
qtde = float(input(f'Insira a quantidade em kg: '))
forma_pgto = int(input(f'Insira a forma de pagamento (1-Cartão Tabajara ou 2-Outros): '))

if tipo == 1:
    nome = 'File Duplo'
    if qtde <= 5:
        valor = qtde * 4.90
    else:
        valor = qtde * 5.80

if tipo == 2:
    nome = 'Alcatra'
    if qtde <= 5:
        valor = qtde * 5.90
    else:
        valor = qtde * 6.80

if tipo == 3:
    nome = 'Picanha'
    if qtde <= 5:
        valor = qtde * 6.90
    else:
        valor = qtde * 7.80

if forma_pgto == 1:
    forma_pgto = 'SIM'
    desconto = valor * 5 / 100
elif forma_pgto == 2:
    forma_pgto = 'NÃO'
    desconto = 0

print()
print('****************************CUPOM FISCAL**************************************')
print('*')
print(f'* Tipo de Carne:.................................................. {nome}')
print(f'* Quantidade de Carne:............................................. {qtde:.3f} Kg')
print(f'* Valor Total:.................................................... R$ {valor:.2f}')
print(f'* Crtão Tabajara:...................................................... {forma_pgto}')
print(f'* Valor do Desconto (5%):........................................... R$ {desconto:.2f}')
print('*')
print(f'* Valor Total a Pagar:............................................. R$ {valor - desconto:.2f}')
print('*')
print('****************************CUPOM FISCAL**************************************')
