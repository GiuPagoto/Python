motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)


# modificando elementos de uma lista
motorcycles[0] = 'ducati'
print(motorcycles)

# acrescentando elementos em uma lista: método append()

# 1.concatenando elementos no final de uma lista

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 2.inserindo elementos em uma lista: método insert()
# em qualquer posição
# desloca os demais valores ima posição à direita

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

# 3.removendo elementos de uma lista

# 3.1 instrução del()
# Se a posição do item que você quer remover de uma lista for conhecida, a instrução del poderá ser usada.
# Se um usuário decidir cancelar a conta em sua aplicação web, você vai querer remover esse usuário da lista de usuários ativos. Você pode remover um item de acordo com sua posição na lista ou seu valor (??)


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# não podemos mais acessar o valor que foi removido da lista após a instrução del ter sido usada.

# 3.2 método pop()
# Às vezes, você vai querer usar o valor de um item depois de removê-lo de uma lista.
# Em uma aplicação web, você poderia remover um usuário de uma lista de membros ativos e então adicioná-lo a uma lista de membros inativos.
# O método pop() remove o último item de uma lista, mas permite que você trabalhe com esse item depois da remoção. O termo pop deriva de pensar em uma lista como se fosse uma pilha de itens e remover um item (fazer um pop) do topo da pilha. Nessa analogia, o topo da pilha corresponde ao final da lista.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcyles = motorcycles.pop()
print(motorcycles) # lista sem o último elemento
print(popped_motorcyles) # elemento que foi retirado da lista

# utilidade desse método:
# ? Suponha que as motocicletas da lista estejam armazenadas em ordem cronológica, de acordo com a época em que fomos seus proprietários. Se for esse o caso, podemos usar o método pop() para exibir uma afirmação sobre a última motocicleta que compramos: motorcycles = ['honda', 'yamaha', 'suzuki'].

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# removendo itens de qualquer posição em uma lista
# método pop() para remover um item de qualquer posição em uma lista se incluir o índice do item que deseja remover 

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# Lembre-se de que, sempre que usar pop(), o item com o qual você trabalhar não estará mais armazenado na lista.

# 3.2 método remove()
# removendo um item de acordo com o valor
# Às vezes, você são saberá a posição do valor que quer remover de uma lista. Se conhecer apenas o valor do item que deseja remover, o método remove() poderá ser usado.
# vamos supor que queremos remover o valor 'ducati' da lista de motocicletas.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# método remove() para trabalhar com um valor que está sendo removido de uma lista. Vamos remover o valor 'ducati' e exibir um motivo para removê-lo da lista

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'

motorcycles.remove(too_expensive)

print(motorcycles)

print("\nA " + too_expensive.title() + " is too expensive for me.")

# NOTA:  O método remove() apaga apenas a primeira ocorrência do valor que você especificar. Se houver a possibilidade de o valor aparecer mais de uma vez na lista, será necessário usar um laço para determinar se todas as ocorrências desse valor foram removidas.


