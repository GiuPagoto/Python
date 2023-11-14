'''
Lugares favoritos: 

Crie um dicionário chamado favorite_places. Pense em três nomes para usar como chaves do dicionário e armazene de um a três ugares favoritos para cada pessoa. Para deixar este exercício um pouco mais interessante, peça a alguns amigos que nomeiem alguns de seus lugares favoritos. Percorra o dicionário com um laço e apresente o nome de cada pessoa e seus lugares favoritos.

'''

favorite_places = {
    'Giovanna': ['Londres', 'Orlando', 'Veneza'],
    'Giullia': ['Fortaleza'],
    'Rebecca' : ['Pequim', 'Santiago']
}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:") 

# percorrer a lista de linguagens favoritas de cada pessoa.
    for place in places:
        print("\t" + place.title())

