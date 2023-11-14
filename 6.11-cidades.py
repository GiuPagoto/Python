'''

Cidades: 

Crie um dicionário chamado cities. Use os nomes de três cidades como chaves em seu dicionário. Crie um dicionário com informações sobre cada cidade e inclua o país em que a cidade está localizada, a população aproximada e um fato sobre essa cidade. As chaves do dicionário de cada cidade devem ser algo como country, population e fact. Apresente o nome de cada cidade e todas as informações que você armazenou sobre ela.

'''

cities = {
    
    'são paulo': {
        'país': 'brasil',
        'população':'44,04 milhões',
        'curiosidade': 'centro financeiro do Brasil',
    },

    'londres': {
        'país': 'inglaterra',
        'população':'8,982 milhões',
        'curiosidade': 'Londres tem carros com velocidade de carruagem',
    },

    'roma': {
        'país': 'italia',
        'população':'2,873 milhões',
        'curiosidade': 'Roma é a maior cidade do país, capital da Itália, da região do Lazio e da província onde está localizada',
    },


}

for city, city_info in cities.items(): 
    print("\n\tCidade: " + city.title())  

    population = city_info['população']
    fact = city_info['curiosidade']

    print("\tPopulação: " + population) 
    print("\tcuriosidade: " + fact.capitalize()) 

