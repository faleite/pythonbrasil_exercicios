"""
19. Faça um Programa que leia um número inteiro menor que 1000
e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e",da vírgula entre outros.
Exemplo:
 - 326 = 3 centenas, 2 dezenas e 6 unidades
 - 12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301,
101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

""" Atualizado """

numero = int(input('Informe um número: '))

centenas_str = dezenas_str = unidades_str = ''

centenas_int, numero = divmod(numero, 100)

partes_numericas = 0

if centenas_int == 1:
    centenas_str = '1 centena'
    partes_numericas += 1
elif centenas_int > 1:
    centenas_str = f'{centenas_int} centenas'
    partes_numericas += 1

dezenas_int, numero = divmod(numero, 10)

if dezenas_int == 1:
    dezenas_str = '1 dezena'
    partes_numericas += 1
elif dezenas_int > 1:
    dezenas_str = f'{dezenas_int} dezenas'
    partes_numericas += 1

if numero == 1:
    unidades_str = '1 unidade'
    partes_numericas += 1
elif numero > 1:
    unidades_str = f'{numero} unidades'
    partes_numericas += 1

if partes_numericas == 0:
    print('Número 0 não possui, centenas, dezenas e unidades')
elif partes_numericas == 1:
    print(centenas_str + dezenas_str + unidades_str)
elif partes_numericas == 3:
    print(f'{centenas_str}, {dezenas_str} e {unidades_str}')
elif partes_numericas == 2:
    if centenas_str != '':
        segunda_parte = dezenas_str + unidades_str
        print(f'{centenas_str} e {segunda_parte}')
    else:
        print(f'{dezenas_str} e {unidades_str}')

""" primeira forma"""
# numero = int(input('Insira um numero menor que 1000: '))
#
# unidade = numero % 10
# dezena = int((numero % 100) / 10)
# centena = int(numero / 100)
#
# print(f'{numero} = {centena} centena(s), {dezena} dezena(s) e {unidade} unidade(s)')
