"""

Ingredientes para uma pizza: 

Escreva um laço que peça ao usuário para fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
fornecido. À medida que cada ingrediente é especificado, apresente uma mensagem informando que você acrescentará esse ingrediente à pizza.

"""

prompt = "\nInsira os ingredientes que você deseja colocar em sua pizza: "

prompt += "\n(Escreva 'quit' quando desejar finalizar o pedido.)"

while True:
    ingredientes = input(prompt)

    if ingredientes == "quit": 
        break 
    else:
        print("O ingrdiente " + ingredientes + "será acrescentado em sua pizza!")