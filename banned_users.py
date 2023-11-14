# VERIFICANDO SE UM VALOR ESTÁ EM UMA LISTA
# verificar se uma lista contém um determinado valor antes de executar uma ação. 
# utilizar a palavra reservada "in"

# código que você poderia escrever para uma pizzaria. 
# lista de ingredientes que um cliente pediu 
# posteriormente, verificar se determinados ingredientes estão na lista 

requested_toppings = ['mushrooms', 'onions', 'pineapple']

print('mushrooms' in requested_toppings) # True
print('pepperoni' in requested_toppings) # False

# VERIFICANDO SE UM VALOR NÃO ESTÁ EM UMA LISTA 
# usar a palavra reservada "not"

# Por exemplo, considere uma lista de usuários que foi impedida de fazer comentários em um fórum. Podemos verificar se um usuário foi banido antes de permitir que essa pessoa submeta um comentário.

banned_users = ['andrew', 'carolina', 'david']

user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")