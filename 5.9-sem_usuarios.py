# SEM USUÁRIOS: Acrescente um teste if em hello_admin.py para garantir que a lista de usuários não esteja vazia.
# • Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns usuários!
# • Remova todos os nomes de usuário de sua lista e certifique-se de que a mensagem correta seja exibida.

users = ['giullia', 'giovanna', 'filomena', 'mel', 'admin']

# apagar a lista
#del users [0:5]

for user in users:      
    if user == 'admin':
        print("Olá, " + user + "! Gostaria de ver um relatório de status?")
    else:
        print("Olá, " + user + "! Obrigada por fazer login novamente.")

if users == []:
    print("Precisamos encontrar alguns usuários!")