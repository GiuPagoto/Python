"""
PESSOAS

Comece com o programa que você escreveu no Exercício 6.1
(página 147). Crie dois novos dicionários que representem pessoas diferentes e armazene os três dicionários em uma lista chamada people. Percorra sua lista de pessoas com um laço. À medida que percorrer a lista, apresente tudo que
você sabe sobre cada pessoa.
 
"""

pessoa = {
    'nome': 'giullia',
    'sobrenome':'pagoto',
    'idade': '24',
    'cidade': 'catanduva',
}

giovanna = {
    'nome': 'giovanna',
    'sobrenome':'pagoto',
    'idade': '27',
    'cidade': 'londres',
}

mel = {
    'nome': 'mel',
    'sobrenome':'pagoto',
    'idade': '12',
    'cidade': 'fortaleza',
}

# criar uma lista de dicionários, em vez de criar uma lista de strings contendo os nomes dos dicionários. 

people = [pessoa, giovanna, mel]

'''
1)

for person in people:
    print("Nome:", person['nome'])
    print("Sobrenome:", person['sobrenome'])
    print("Idade:", person['idade'])
    print("Cidade:", person['cidade'])
    print()  # Uma linha em branco para separar as informações de pessoas diferentes

'''

# Percorra a lista e exiba as informações de cada pessoa
for person in people:
    print("Informações sobre a pessoa:")
    for key, value in person.items():
        print(f"{key.capitalize()}: {value}")
    print()  # Uma linha em branco para separar as informações de pessoas diferentes




    

