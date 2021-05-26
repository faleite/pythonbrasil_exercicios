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

cod100 = cod101 = cod102 = cod103 = cod104 = cod105 = 0

while True:
    codigo = int(input('Informe o código do pedido: '))
    if codigo == 0:
        break
    qtd = int(input('Informe a quantidade: '))

    if codigo == 100:
        cod100 = qtd*1.20
        print(f'Valor a ser pago: R$ {cod100:.2f}')
    if codigo == 101:
        cod101 = qtd*1.30
        print(f'Valor a ser pago: R$ {cod101:.2f}')
    if codigo == 102:
        cod102 = qtd*1.50
        print(f'Valor a ser pago: R$ {cod102:.2f}')
    if codigo == 103:
        cod103 = qtd*1.20
        print(f'Valor a ser pago: R$ {cod103:.2f}')
    if codigo == 104:
        cod104 = qtd*1.30
        print(f'Valor a ser pago: R$ {cod104:.2f}')
    if codigo == 105:
        cod105 = qtd*1.00
        print(f'Valor a ser pago: R$ {cod105:.2f}')

soma = cod100 + cod101 + cod102 + cod103 + cod104 + cod105
print(f'Valor total do pedido: R$ {soma:.2f}')
