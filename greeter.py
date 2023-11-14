#name = input("Please enter your name: ")

#print("Hello, " + name + "!")


""" 

um prompt que seja maior que uma linha. Por exemplo, talvez você queira explicar ao usuário por que está pedindo determinada entrada. Você pode armazenar seu prompt em
uma variável e passá-la para a função input(). Isso permite criar seu prompt com várias linhas e escrever uma instrução input() clara.

"""

# A primeira linha armazena a parte inicial da mensagem na variável prompt.
#prompt = "If you tell us who you are, we can personalize the message you see."

# Na segunda linha, o operador += acrescenta a nova string no final da string que estava armazenada em prompt. 
#prompt += "\nWhat is your first name? "

#name = input(prompt)

#print("\nHello, " + name + "!")

""" 

Se usarmos a função input(), Python interpretará tudo que o usuário fornecer como uma string. Considere a sessão de interpretador a seguir, que pergunta a idade do usuário

"""
#age = input("How old are you? ")

#print(age)

""" 

Se tudo que você quiser fazer é exibir a entrada, isso funcionará bem. Entretanto, se tentar usar a entrada como um número, você obterá um erro.

Python gera um erro, pois não é capaz de comparar uma string com um inteiro: a string '21' armazenada em age não pode ser comparada ao valor numérico 18.

"""
#age = input("How old are you? ")

#print(age)

#print(age >= 18)

""" 

Podemos resolver esse problema usando a função int(), que diz a Python para tratar a entrada como um valor numérico. A função int() converte a representação em string de um número em uma representação numérica

"""

age = input("How old are you? ")

print(age)

age = int(age)

print(age >= 18)