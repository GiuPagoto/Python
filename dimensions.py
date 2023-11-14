# TUPLAS: 
# As listas funcionam bem para armazenar conjuntos de itens que podem mudar durante a vida de um programa. A capacidade de modificar listas é particularmente importante quando trabalhamos com uma lista de usuários em um site ou com uma lista de personagens em um jogo. No entanto, às vezes, você vai querer criar uma lista de itens que não poderá mudar. As tuplas permitir fazer exatamente isso. Python refere-se a valores que não podem mudar como imutáveis, e uma lista imutável é chamada de tupla.

# Uma tupla se parece exatamente com uma lista, exceto por usar parênteses no lugar de colchetes. Depois de definir uma tupla, podemos acessar elementos individuais usando o índice de cada item, como faríamos com uma lista.

# Por exemplo, se tivermos um retângulo que sempre deva ter determinado tamanho, podemos garantir que seu tamanho não mudará colocando as dimensões em uma tupla.

dimensions = (200,50)

print(dimensions[0])
print(dimensions[1])

# se tentarmos alterar um dos itens da tupla dimensions
# dimensions[0] = 250
# Python nos informa que não podemos atribuir um novo valor a um item em uma tupla

# PERCORRENDO TODOS OS VALORES DE UMA TUPLA COM UM LAÇO

for dimension in dimensions:
    print(dimension)

# SOBRESCREVENDO UMA TUPLA

# Embora não seja possível modificar uma tupla, podemos atribuir um novo valor a uma variável que armazena uma tupla. Portanto, se quiséssemos alterar nossas dimensões, poderíamos redefinir a tupla toda:

print("Original dimensions: ")
for dimension in dimensions: 
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

