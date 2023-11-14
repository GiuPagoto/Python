# Uma lista de dicionários

'''
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens: 
    print(alien)
'''


'''

# Cria uma lista vazia para armazenar alienígenas 

aliens = []

# Cria 30 alienígenas verdes 

for alien_number in range(30): 
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Mostra os 5 primeiros alienígenas

for alien in aliens[:5]:
    print(alien) 

print("...")

# Mostra quantos alienígenas foram criados

print("Total number of aliens: " + str(len(aliens))) 

'''

'''
Todos esses alienígenas têm as mesmas características, mas Python
considera cada um como um objeto diferente, o que nos permite
modificar cada alienígena individualmente.

Como podemos trabalhar com um conjunto de alienígenas como esse?
Suponha que um aspecto do jogo consista em fazer alguns alienígenas
mudarem de cor e moverem-se mais rápido à medida que o jogo
prosseguir. Quando for o momento de mudar de cor, podemos usar um
laço for e uma instrução if para alterar a cor dos alienígenas. Por
exemplo, para mudar os três primeiros alienígenas para amarelo, com
velocidade média, valendo dez pontos cada, podemos fazer o seguinte:

'''


aliens = []

for alien_number in range(30): 
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[0:5]:
    print(alien)

print("...")



'''

expandir esse laço acrescentando um bloco elif que
transforme alienígenas amarelos em alienígenas vermelhos e rápidos,
que valem 15 pontos cada.

'''

for alien in aliens:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[0:5]:
    print(alien)

print("...")

'''

É comum armazenar vários dicionários em uma lista quando cada
dicionário tiver diversos tipos de informação sobre um objeto. Por exemplo, podemos criar um dicionário para cada usuário de um site, como fizemos em user.py, e armazenar os dicionários individuais em uma lista chamada users. Todos os dicionários da lista devem ter uma estrutura idêntica para que possamos percorrer a lista com um laço e trabalhar com cada objeto representado por um dicionário do mesmo
modo.

'''