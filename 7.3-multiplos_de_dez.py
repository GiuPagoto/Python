""" 

Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o número é múltiplo de dez ou não.

"""

numero = input("Informe um número para saber se é múltiplo de 10: ")

numero = int(numero)

if numero % 10 == 0:
    print("\nO número  " + str(numero) + " é múltiplo de 10.")
else:
    print("\nO número " + str(numero) + " não é múltiplo de 10.")