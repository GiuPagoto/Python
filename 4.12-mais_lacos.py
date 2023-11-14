# MAIS LAÇOS:  Todas as versões de foods.py nesta seção evitaram usar laços for para fazer exibições a fim de economizar espaço. Escolha uma versão de foods.py e escreva dois laços for para exibir cada lista de comidas.

my_foods = ['pizza', 'lasanha', 'hamburguer']
friend_foods = my_foods[:]


print("My favorite foods are: ")
for my_favorite_food in my_foods:
    print(my_favorite_food)

print("\nMy friend´s favorite foods are: ")
for my_friend_favorite_food in friend_foods:
    print(my_friend_favorite_food)


