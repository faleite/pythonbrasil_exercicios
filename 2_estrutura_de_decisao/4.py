""" 4. Faça um Programa que verifique se
uma letra digitada é vogal ou consoante.
"""

letra = input('Insira uma letra: ')
vogal = 'aeiouAEIOU'

if letra in vogal:
    print('Esta letra é uma vogal!')
else:
    print('Esta letra é uma consoante!')
