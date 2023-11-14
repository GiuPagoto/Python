""" 

Uma ferramenta útil para trabalhar com informações numéricas é o operador de módulo (%), que divide um número por outro e devolve o resto: 

>>> 4 % 3
1
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1

Quando um número é divisível por outro, o resto é 0, portanto o operador de módulo sempre devolve 0 nesse caso. Podemos usar esse fato para determinar se um número é par ou ímpar

"""

number = input("Enter a number, and I'll tell you if it's even or odd: ")

number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

