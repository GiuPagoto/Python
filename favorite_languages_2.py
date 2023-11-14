# lista em um dicionário

# Você pode aninhar uma lista em um dicionário sempre que quiser que mais de um valor seja associado a uma única chave em um dicionário. No exemplo anterior das linguagens de programação favoritas, se armazenássemos as respostas de cada pessoa em uma lista, elas poderiam escolher mais de uma linguagem predileta. Se percorrermos o dicionário com um laço, o valor associado a cada pessoa será uma lista das linguagens, e não uma única linguagem. No laço for do dicionário, usamos outro laço for para percorrer a lista de linguagens associada a cada pessoa.


# o valor associado a cada nome agora é uma lista
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

# usamos uma variável de nome languages para armazenar cada valor do dicionário, pois sabemos que esse valor será uma lista
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:") 

# percorrer a lista de linguagens favoritas de cada pessoa.
    for language in languages:
        print("\t" + language.title())
