# lista dos dez primeiros quadrados perfeitos (isto é, o quadrado de cada inteiro de 1 a 10)



# forma 1

squares = [] # lista vazia 

for value in range(1,11): # percorrer cada valor de 1 a 10 usando a função range()
    square = value**2 # o valor atual é elevado ao quadrado e armazenado na variável square
    squares.append(square) # cada novo valor de square é concatenado à lista squares
    print(squares) # a lista de quadrados é exibida

# forma 2

squares = [] # lista vazia 

for value in range(1,11): # percorrer cada valor de 1 a 10 usando a função range()
    square = value**2 # o valor atual é elevado ao quadrado e armazenado na variável square
    squares.append(square) # cada novo valor de square é concatenado à lista squares
    
print(squares) # quando o laço acaba de executar, a lista de quadrados é exibida

# forma 3: código mais conciso 

squares = []

for value in range(1,11):
    squares.append(value**2) # Cada valor do laço é elevado ao quadrado e, então, é imediatamente concatenado à lista de quadrados.

print(squares)


# estatísticas simples com uma lista de números

digits = [1,2,3,4,5,6,7,8,9,0]

print(min(digits))
print(max(digits))
print(sum(digits))


# list comprehensions 
# A abordagem descrita antes para gerar a lista squares usou três ou quatro linhas de código. Uma list comprehension (abrangência de lista) permite gerar essa mesma lista com apenas uma linha de código. Uma list comprehension combina o laço for e a criação de novos elementos em uma linha, e concatena cada novo elemento automaticamente.

squares = [value**2 for value in range(1,11)]
print(squares)