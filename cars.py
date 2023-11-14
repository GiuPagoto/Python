# supor que todos os valores da lista usam letras minúsculas.



# método sort()
# ordenando uma lista de forma permanente com o método sort()
# ordem alfabética

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.sort()
print(cars)

# ordem alfabética inversa
# argumento: reverse=True

cars.sort(reverse=True)
print(cars)


# função sorted()
# ordenando umalistatemporariamentecomafunção sorted()
# Para preservar a ordem original de uma lista, mas apresentá-la de forma ordenada, podemos usar a função sorted(). A função sorted() permite exibir sua lista em uma ordem em particular, mas não afeta a ordem propriamente dita da lista.

cars = ['bmw', 'audi', 'toyota', 'subaru']

print('Here is the original list: ')
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)

# Essa função também pode aceitar um argumento reverse=True se você quiser exibir uma lista em ordem alfabética inversa.

# NOTA: Ordenar uma lista em ordem alfabética é um pouco mais complicado quando todos os valores não utilizam letras minúsculas. Há várias maneiras de interpretar letras maiúsculas quando decidimos por uma sequência de ordenação, e especificar a ordem exata pode apresentar um nível de complexidade maior que aquele com que queremos lidar no momento. No entanto, a maior parte das abordagens à ordenação terá diretamente como base o que aprendemos nesta seção.


# reverse()
# exibindo uma lista em ordem inversa 
# Para inverter a ordem original de uma lista, podemos usar o método reverse(). Se armazenarmos originalmente a lista de carros em ordem cronológica, de acordo com a época em que fomos seus proprietários, poderemos facilmente reorganizar a lista em ordem cronológica inversa:

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# Observe que reverse() não reorganiza em ordem alfabética inversa; ele simplesmente inverte a ordem da lista.
# O método reverse() muda a ordem de uma lista de forma permanente, mas podemos restaurar a ordem original a qualquer momento aplicando reverse() à mesma lista uma segunda vez.


# len()
# Descobrindo o tamanho de uma lista
# determinar a quantidade de dados que você precisa administrar em uma visualização ou descobrir o número de usuários registrados em um site, entre outras tarefas

print(len(cars))

# NOTA: Python conta os itens de uma lista começando em um, portanto você não deverá se deparar com nenhum erro de deslocamento de um ao determinar o tamanho de uma lista.