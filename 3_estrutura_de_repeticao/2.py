"""
2. Faça um programa que leia um nome de usuário e a sua senha
e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
while True:
    nome = str(input('Nome de usuário: '))
    senha = input('Senha: ')

    if nome != senha:
        break
    else:
        print('Erro. A senha deve ser diferente do usuário')
