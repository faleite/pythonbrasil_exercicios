"""
43. O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

while True:
    codigo = int(input('Informe o código do pedido: '))
    if codigo == 0:
        break
    qtd = int(input('Informe a quantidade: '))

    if codigo == 100:
        print(f'Valor a ser pago: {qtd*1.20}')
    if codigo == 101:
        print(f'Valor a ser pago: {qtd*1.30}')
    if codigo == 102:
        print(f'Valor a ser pago: {qtd*1.50}')
    if codigo == 103:
        print(f'Valor a ser pago: {qtd*1.20}')
    if codigo == 104:
        print(f'Valor a ser pago: {qtd*1.30}')
    if codigo == 105:
        print(f'Valor a ser pago: {qtd*1.00}')
