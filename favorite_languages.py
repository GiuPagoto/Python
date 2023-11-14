# Percorrer todos os pares chave-valor com um laço funciona bem, em particular, para dicionários como o do exemplo em favorite_languages.py.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items(): 
    print(name.title() + 
          "'s favorite language is " + 
          language.title() + '.') 

# PERCORRENDO TODAS AS CHAVES DE UM DICIONÁRIO COM UM LAÇO
# O método keys() é conveniente quando não precisamos trabalhar com todos os valores de um dicionário. Vamos percorrer o dicionário favorite_languages com um laço e exibir os nomes de todos que responderam à enquete.

#extrair todas as chaves do dicionário favorite_languages e armazená-las, uma de cada vez, na variável name.
for name in favorite_languages.keys():
    print("\n" + name.title())

# Percorrer as chaves, na verdade, é o comportamento-padrão quando percorremos um dicionário com um laço, portanto este código produzirá a mesma saída se escrevêssemos: for name in favorite_languages: em vez de: for name in favorite_languages.keys():
for name in favorite_languages:
    print("\n" + name.title())

# Podemos acessar o valor associado a qualquer chave que nos interessar no laço usando a chave atual.

friends = ['phil', 'sarah']

for name in favorite_languages.keys():

    print("\n" + name.title())
    if name in friends:
        print("\nHi " + name.title() + 
              " , I see your favorite language is " + favorite_languages[name].title() + '!')

# usar o método keys() para descobrir se uma pessoa em particular participou da enquete. Dessa vez, vamos ver se Erin respondeu à enquete:

# O método keys() não serve apenas para laços: na verdade, ele devolve uma lista de todas as chaves, e a primeira linha simplesmente verifica se 'erin' está nessa lista. Como ela não está, uma mensagem é exibida convidando-a a participar da enquete: Erin, please take our poll!

if 'erin' not in favorite_languages.keys():

    print("\nErin, please take our poll!")

# PERCORRENDO AS CHAVES DE UM DICIONÁRIO EM ORDEM USANDO UM LAÇO
# ordenar as chaves à medida que são devolvidas no laço for.
# usar a função sorted() para obter uma cópia ordenada das chaves:

# a função sorted() está em torno do método dictionary.keys(). Isso diz a Python para listar todas as chaves do dicionário e ordenar essa lista antes de percorrê-la com um laço. A saída mostra os nomes de todos que responderam à enquete, exibidos de forma ordenada:
for name in sorted(favorite_languages.keys()):

    print("\n" + name.title() + ", thank you for taking the poll.")

# PERCORRENDO TODOS OS VALORES DE UM DICIONÁRIO COM UM LAÇO
# Se você estiver mais interessado nos valores contidos em um dicionário, o método values() pode ser usado para devolver uma lista de valores sem as chaves.
# Por exemplo, suponha que queremos apenas uma lista de todas as linguagens escolhidas em nossa enquete sobre linguagens de programação, sem o nome da pessoa que escolheu cada linguagem:


print("\nThe following languages have been mentioned: ")
for language in favorite_languages.values():

    print("\n" + language.title())

# Essa abordagem extrai todos os valores do dicionário, sem verificar se há repetições.

# Para ver cada linguagem escolhida sem repetições, podemos usar um conjunto (set). Um conjunto é semelhante a uma lista, exceto que cada item de um conjunto deve ser único:

print("\nThe following languages have been mentioned: ")

for language in set(favorite_languages.values()):
    print("\n" + language.title())


