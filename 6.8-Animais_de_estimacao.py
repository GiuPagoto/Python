'''
Animais de estimação: 

Crie vários dicionários, em que o nome de cada dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua o tipo do animal e o nome do dono. Armazene esses dicionários em uma lista chamada pets. Em seguida, percorra sua lista com um laço e, à medida que fizer isso, apresente tudo que você sabe sobre cada animal de estimação.

'''

mel = {
    'raça' : 'pincher',
    'dono' : 'giovanna',
}

filomena = {
    'raça' : 'shihtzu',
    'dono' : 'giullia',
}

rhanyra = {
    'raça' : 'underdog',
    'dono' : 'rebecca',
}

pets = [mel, filomena, rhanyra]

# Percorra a lista e exiba as informações de cada pessoa
for dog in pets:
    print("Informações sobre o pet:")
    for key, value in dog.items():
        print(f"{key.capitalize()}: {value.title()}")
    print()  # Uma linha em branco para separar as informações de pessoas diferentes
