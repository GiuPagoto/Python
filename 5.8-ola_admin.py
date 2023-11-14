# OLA ADMIN: Crie uma lista com cinco ou mais nomes de usuários, incluindo o nome 'admin'. Suponha que você esteja escrevendo um código que exibirá uma saudação a cada usuário depois que eles fizerem login em um site. Percorra a lista com um laço e mostre uma saudação para cada usuário: 
# • Se o nome do usuário for 'admin', mostre uma saudação especial, por exemplo, Olá admin, gostaria de ver um relatório de status?
#  Caso contrário, mostre uma saudação genérica, como Olá Eric, obrigado por fazer login novamente.

users = ['giullia', 'giovanna', 'filomena', 'mel', 'admin']

for user in users: 
    if user == 'admin':
        print("Olá, " + user + "! Gostaria de ver um relatório de status?")
    else:
        print("Olá, " + user + "! Obrigada por fazer login novamente.")

