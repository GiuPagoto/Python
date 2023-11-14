# Um dicionário em um dicionário

# Podemos aninhar um dicionário em outro dicionário, mas o código poderá ficar complicado rapidamente se isso for feito. Por exemplo, se você tiver vários usuários em um site, cada um com um nome único, os nomes dos usuários poderão ser usados como chaves em um dicionário. Você poderá então armazenar informações sobre cada usuário usando um dicionário como o valor associado a cada nome de usuário. Na listagem a seguir, armazenamos três informações sobre cada usuário: seu primeiro nome, o sobrenome e a localidade. Acessaremos essas informações percorrendo os nomes dos usuários em um laço e o dicionário de informações associado a cada nome de usuário

users = {
    'aeintein': {'first': 'albert', 'last': 'eistein', 'location': 'princeton'},

    'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris'},

}

for username, user_info in users.items(): 
    print("\nUsername: " + username)  

full_name = user_info['first'] + " " + user_info['last']
location = user_info['location']

print("\tFull name: " + full_name.title()) 
print("\tLocation: " + location.title()) 