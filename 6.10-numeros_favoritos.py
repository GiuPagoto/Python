'''

Números favoritos: 

Modifique o seu programa do Exercício 6.2 (página 147) para que cada pessoa possa ter mais de um número favorito. Em seguida, apresente o nome de cada pessoa, juntamente com seus números favoritos.

'''

favorite_numbers = {
    'celso': ['55', '30', '28'],
    'sara': ['20', '22', '24'],
    'giovanna': ['24', '15'],
    'giullia': ['12'],
}

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite places are:") 

# percorrer a lista de linguagens favoritas de cada pessoa.
    for number in numbers:
        print("\t" + number)