# MAIS CONVIDADOS: Você acabou de encontrar uma mesa de jantar maior,portanto agora tem mais espaço disponível. Pense em mais três convidados para o jantar.

# Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente uma instrução print no final de seu programa informando às pessoas que você encontrou uma mesa de jantar maior.

#  Utilize insert() para adicionar um novo convidado no início de sua lista.

# Utilize insert() para adicionar um novo convidado no meio de sua lista.

# Utilize append() para adicionar um novo convidado no final de sua lista.

# Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que está em sua lista.

dinner_wiht = ['Jesus', 'Clarice' ,'Alex Turner']

mensagem = dinner_wiht[0] + ", o Senhor gostaria de jantar comigo hoje?"
print(mensagem)

mensagem = "Vó " + dinner_wiht[1] + ", a senhora gostaria de jantar comigo hoje?"
print(mensagem)

mensagem = dinner_wiht[2] + ", você gostaria de jantar comigo hoje?"
print(mensagem)


print("\nApesar do meu convite educado, o  " + dinner_wiht[2].upper() + ' não aceitou comparecer ao jantar, porque tinha um show para fazer em Londres.')

# modificando elementos de uma lista
dinner_wiht[2] = 'MEL'

print("\nMas, felizmente, eu reencontrei a " + dinner_wiht[2] + ' que é uma companhia 1000 vezes melhor. E assim, refiz o convite para todos os meus convidados: ')

mensagem = dinner_wiht[0] + ", o Senhor gostaria de jantar comigo hoje?"
print(mensagem)

mensagem = "Vó " + dinner_wiht[1] + ", a senhora gostaria de jantar comigo hoje?"
print(mensagem)

mensagem = dinner_wiht[2] + ", você quer melão?"
print(mensagem)

print("\nE todos aceitaram e jantaram comigo.")

print("\nPara melhorar a situação, quando estávamos no caminho para o restaurante, fui informada pela recepcionista que havia uma mesa maior. E disse para os meus convidados: " + "\n\t'Pessoal, tem uma mesa maior e por isso vou convidar mais algumas pessoas.'")

# inserir um novo convidado no início da lista:

dinner_wiht.insert(0, 'Filomena')
print(dinner_wiht)

# inserir um novo convidado no meio da lista:

dinner_wiht.insert(2, 'Tata')
print(dinner_wiht)

# inserir um novo convidado no final da lista 

dinner_wiht.append('Gustavo')
print(dinner_wiht)

print("\nE, então refiz o convite para todos: ")

mensagem = dinner_wiht[0] + ", você quer gostosinho?"
print(mensagem)

mensagem = dinner_wiht[1] + ", o Senhor gostaria de jantar comigo hoje?"
print(mensagem)

mensagem = dinner_wiht[2] + ", vamos sair para jantar hoje?"
print(mensagem)

mensagem = "Vó " + dinner_wiht[3] + ", a senhora gostaria de jantar comigo hoje?"
print(mensagem)

mensagem = dinner_wiht[4] + ", você quer melão?"
print(mensagem)

mensagem = dinner_wiht[5] + ", vamos comigo e com a tata em um jantar?"
print(mensagem)

print("\nE jantamos todos juntos.")






