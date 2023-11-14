""" 

Para sair de um laço while de imediato, sem executar qualquer código restante no laço, independentemente do resultado de qualquer teste condicional, utilize a instrução break. A instrução break direciona o fluxo de seu programa; podemos usá-la para controlar quais linhas de código são ou não são executadas, de modo que o programa execute apenas o código que você quiser, quando você quiser.

considere um programa que pergunte aos usuários os nomes de lugares que eles já visitaram. Podemos interromper o laço while nesse programa chamando break assim que o usuário fornecer o valor 'quit'

"""

prompt = "\nPlease enter the name of a city you have visited: "

prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == "quit": 
        break 
    else:
        print("I'd love to go to " + city.title() + "!")


""" 

Você pode usar a instrução break em qualquer laço de Python. Por exemplo, break pode ser usado para sair de um laço for que esteja percorrendo uma lista ou um dicionário.

"""