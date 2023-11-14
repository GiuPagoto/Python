# TRABALHANDO COM PARTE DE UMA LISTA
# trabalhar com um grupo específico de itens de uma lista, que Python chama de fatia.

# FATIANDO UMA LISTA
# Para criar uma fatia, especifique o índice do primeiro e do último elemento com os quais você quer trabalhar. Como ocorre na função range(), Python para em um item antes do segundo índice que você especificar. Para exibir os três primeiros elementos de uma lista, solicite os índices de 0 a 3; os elementos 0, 1 e 2 serão devolvidos.

players = ['Celso', 'Sara', 'Giovanna', 'Gustavo', 'Giullia']

print(players[0:3]) # posições de 0 a 2
print(players[1:4]) # posições de 1 a 3
print(players[:4])  # posições de 0 a 3
print(players[2:])  # posições de 2 até o final 

print(players[-3:]) # Esse código exibe os nomes dos três últimos jogadores e continuaria a funcionar à medida que a lista de jogadores mudar de tamanho.
# os nomes dos três últimos jogadores até o final da lista

# PERCORRENDO UMA FATIA COM UM LAÇO
# usar uma fatia em um laço for se quiser percorrer um subconjunto de elementos de uma lista. No próximo exemplo, percorreremos os três primeiros jogadores e exibiremos seus nomes como parte de uma lista simples:

players = ['Celso', 'Sara', 'Giovanna', 'Gustavo', 'Giullia']

print("Here are the first three players on my team: ")

for player in players[:3]: # Em vez de percorrer a lista inteira de jogadores em u, Python percorre somente os três primeiros nomes
    print(player.title())

# As fatias são muito úteis em várias situações. Por exemplo, quando criar um jogo, você poderia adicionar a pontuação final de um jogador em uma lista sempre que esse jogador acabar de jogar. Seria possível então obter as três pontuações mais altas de um jogador ordenando a lista em ordem decrescente e obtendo uma lista que inclua apenas as três primeiras pontuações. Ao trabalhar com dados, você pode usar fatias para processar seus dados em porções de tamanho específico. Quando criar uma aplicação web, fatias poderiam ser usadas para exibir informações em uma série de páginas, com uma quantidade apropriada de informações em cada página.




