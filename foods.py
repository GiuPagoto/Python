# COPIANDO UMA LISTA
# começar com uma lista existente e criar uma lista totalmente nova com base na primeira.
# Para copiar uma lista, podemos criar uma fatia que inclua a lista original inteira omitindo o primeiro e o segundo índices ([:]).

# Por exemplo, suponha que temos uma lista de nossos alimentos prediletos e queremos criar uma lista separada de comidas que um amigo gosta. Esse amigo gosta de tudo que está em nossa lista até agora, portanto podemos criar sua lista copiando a nossa.

my_foods = ['pizza', 'lasanha', 'hamburguer']
friend_foods = my_foods[:]

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend´s favorite foods are: ")
print(friend_foods)

# acrescentando uma comida em cada lista

my_foods.append("bolo")
friend_foods.append("gelato")

print("\nMy favorite foods are: ")
print(my_foods)

print("\nMy friend´s favorite foods are: ")
print(friend_foods)

# o que acontece quando tentamos copiar uma lista sem usar uma fatia:
# ISSO NÃO FUNCIONA: 

my_foods = ['pizza', 'lasanha', 'hamburguer']

friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend´s favorite foods are: ")
print(friend_foods)

# Em vez de armazenar uma cópia de my_foods em friend_foods, definimos que friend_foods é igual a my_foods. Essa sintaxe, na verdade, diz a Python para conectar a nova variável friend_foods à lista que já está em my_foods, de modo que, agora, as duas variáveis apontam para a mesma lista. Como resultado, quando adicionamos 'cannoli' em my_foods, essa informação aparecerá em friend_foods. De modo semelhante, 'ice cream' aparecerá nas duas listas, apesar de parecer que foi adicionada somente em friend_foods.



