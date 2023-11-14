""" 

Lugares em um restaurante: 

Escreva um programa que pergunte ao usuário quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que oito, exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso contrário, informe que sua mesa está pronta.

"""

pessoas = input("Quantas pessoas participarão do seu jantar? ")

pessoas = int(pessoas)

if pessoas > 8:
    print("\nVocês deverão esperar uma mesa.")
else:
    print("\nSua mesa está pronta!")
