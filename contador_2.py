""" 

Em vez de sair totalmente de um laço sem executar o restante de seu código, podemos usar a instrução continue para retornar ao início, com base no resultado de um teste condicional. Por exemplo, considere um laço que conte de 1 a 10, mas apresente apenas os números ímpares desse intervalo

"""

current_number = 0

while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        continue
    
    print(current_number)