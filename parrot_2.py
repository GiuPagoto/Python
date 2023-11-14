""" 

Deixando o usuário decidir quando quer sair

Podemos fazer o programa parrot.py executar enquanto o usuário quiser colocar a maior parte dele em um laço while. Definiremos um valor de saída e então deixaremos o programa executando enquanto o usuário não tiver fornecido o valor de saída.

"""

# definimos um prompt que informa quais são as duas opções ao usuário: fornecer uma mensagem ou o valor de saída (nesse caso, é 'quit').
prompt = "Tell me something, and I will repeat it back to you: "

prompt += "\nEnter 'quit' to end the program."


""" 
variável message v para armazenar o valor que o usuário fornecer.

Definimos message como uma string vazia, "", de modo que
Python tenha algo para conferir na primeira vez que alcançar a linha com while. Na primeira vez que o programa executar e Python alcançar a instrução while, ele deverá comparar o valor de message com 'quit', mas o usuário ainda não forneceu nenhuma entrada. Se Python não tiver nada para comparar, ele não será capaz de continuar executando o programa. Para
resolver esse problema, garantimos que message receba um valor inicial. Embora seja apenas uma string vazia, ela fará sentido para Python e permitirá que a comparação que faz o laço while funcionar seja feita.

"""
message = ""

#laço while executa enquanto o valor de message não for 'quit'.
while message != 'quit':
    message = input(prompt)
    print(message)

""" 
Na primeira passagem pelo laço, message é apenas uma string vazia, portanto Python entra no laço. Em message = input(prompt), Python exibe o prompt e espera o usuário fornecer uma entrada. O que quer que seja fornecido será armazenado em message e exibido; em seguida, Python avalia novamente a condição na instrução while. Desde que o usuário não tenha fornecido a palavra 'quit', o prompt será exibido novamente e
Python esperará mais entradas. Quando o usuário finalmente digitar 'quit', Python para de executar o laço while e o programa termina: Tell me something, and I will repeat it back to you: Enter 'quit' to end the program.

"""