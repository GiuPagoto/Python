# PERCORRENDO UM DICIONÁRIO COM UM LAÇO
# Como um dicionário pode conter uma grande quantidade de dados, Python permite percorrer um dicionário com um laço. Dicionários podem ser usados para armazenar informações de várias maneiras; assim, há diversos modos diferentes de percorrê-los com um laço. Podemos percorrer todos os pares chave-valor de um dicionário usando suas chaves ou seus valores.

# PERCORRENDO TODOS OS PARES CHAVE-VALOR COM UM LAÇO
# dicionário projetado para armazenar informações sobre um usuário em um site.
# O dicionário a seguir armazenará o nome de usuário, o primeiro nome e o sobrenome de uma pessoa:

user_0 = {'username': 'giupagoto',
          'first_name': 'giullia',
          'last_name': 'pagoto',}


# para escrever um laço for para um dicionário, devemos criar nomes para as duas variáveis que armazenarão a chave e o valor de cada par chave-valor.
# A segunda metade da instrução for inclui o nome do dicionário, seguido do método items(), que devolve uma lista de pares chave-valor. O laço for então armazena cada um desses pares nas duas variáveis especificadas.  

#for key, value in user_0.items(): 
    
    #  O "\n" na primeira instrução print garante que uma linha em branco seja inserida antes de cada par chave-valor na saída

    #print("\nKey: " + key)
    #print("Value: " + value)

for key, value in user_0.items(): 
    if key == 'username':
        print("\nKey: " + key)
        print("Value: " + value)
    else:
        print("\nKey: " + key)
        print("Value: " + value.title())
