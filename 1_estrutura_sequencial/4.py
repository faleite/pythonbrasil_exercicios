"""4. Faça um Programa que peça as 4 notas bimestrais e mostre a média."""

nota_1 = float(input('Insira a primeira nota do bimestre: '))
nota_2 = float(input('Insira a segunda nota do bimestre: '))
nota_3 = float(input('Insira a terceira nota do bimestre: '))
nota_4 = float(input('Insira a quarta nota do bimestre: '))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print(f'A nota média do bimestre é: {media:.2}')
