# TODAS AS FUNÇÕES: Pensa em algo que você poderia armazenar em uma lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países, cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que crie uma lista contendo esses itens e então utilize cada função apresentada neste capítulo pelo menos uma vez.

# lista

cidades_que_morei = ['Americana', 'Barbacena', 'Recife', 'Fortaleza', 'São Caetano', 'Catanduva']

# acessando elementos de uma lista

print(cidades_que_morei[0]) # Americana

print(cidades_que_morei[1]) # Barbacena

print(cidades_que_morei[2]) # Recife

print(cidades_que_morei[3]) # Fortaleza

print(cidades_que_morei[4]) # São Caetano

print(cidades_que_morei[5]) # Catanduva


print(cidades_que_morei[-1]) # Catanduva

print(cidades_que_morei[-2]) # São Caetano

print(cidades_que_morei[-3]) # Fortaleza

print(cidades_que_morei[-4]) # Recife

print(cidades_que_morei[-5]) # Barbacena

print(cidades_que_morei[-6]) # Americana

# Usando valores individuais de uma lista

message = "A primeira cidade em que eu morei foi " + cidades_que_morei[0].upper() + "."
print(message)

# Modificando elemento de uma lista 

print(cidades_que_morei)

cidades_que_morei[3] = 'Maranhão'
print(cidades_que_morei)

# Acrescentando elementos em uma lista 

# concatenando elementos no final de uma lista

cidades_que_morei.append('Fortaleza')
print(cidades_que_morei)

# inserinto elementos em uma lista (em qualquer posição)

cidades_que_morei.insert(4, 'Olimpia')
print(cidades_que_morei)

# removendo elementos de uma lista 

# removendo um item usando a instrução del 

del cidades_que_morei[4]
print(cidades_que_morei)

# removendo um item com o método pop()

popped_cidades_que_morei = cidades_que_morei.pop()
print(popped_cidades_que_morei)
print(cidades_que_morei)

# removendo itens de qualquer posição em uma lista

cidades_que_morei.pop(1)
print(cidades_que_morei)

# removendo um item de acordo com o valor

cidades_que_morei.remove("São Caetano")
print(cidades_que_morei)

# ordenando uma lista de forma permanente com o método sort()

cidades_que_morei.sort()
print(cidades_que_morei)

cidades_que_morei.sort(reverse = True)
print(cidades_que_morei)

# ordenando uma lista temporariamente com a função sorted()

print(sorted(cidades_que_morei))

print(sorted(cidades_que_morei, reverse = True))

# exibindo uma lista em ordem inversa 

cidades_que_morei.reverse()
print(cidades_que_morei)

# descobrindo o tamanho de uma lista

print(len(cidades_que_morei))

