# MINHAS PIZZAS, SUAS PIZZAS: Comece com seu programa do Exercício 4.1. Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.

pizzas = ['lombinho', 'pepperoni', 'marguerita']

for pizza in pizzas:
    print(pizza + '\n')

for pizza in pizzas:
    print("um dos meus sabores preferidos de pizza é " + pizza + '.\n')

print("Só de falar sobre isso, já estou com fome.\nPor isso, vou comprar três pizzas hoje, uma de lombinho, uma de pepperoni e uma marguerita!\nE essa será essa o meu jantar, nada saúdavel.\nPORQUE EU AMO PIZZA!")

friend_pizzas = pizzas[:]

# • Adicione uma nova pizza à lista original.

pizzas.append("mussarela")
print(pizzas)

friend_pizzas.append("portuguesa")
print(friend_pizzas)

# • Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas favoritas são:; em seguida, utilize um laço for para exibir a primeira lista. Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize um laço for para exibir a segunda lista. Certifique-se de que cada pizza nova esteja armazenada na lista apropriada.

print("Minhas pizzas favoritas são: ")
for minha_pizza in pizzas:
    print(minha_pizza)

print("As pizzas favoritas de meu amigo são: ")
for friend_pizza in friend_pizzas:
    print(friend_pizza)