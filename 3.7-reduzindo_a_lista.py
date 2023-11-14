# REDUZINDO A LISTA DE CONVIDADOS: Você acabou de descobrir que sua nova mesa de jantar não chegará a tempo para o jantar e tem espaço para somente dois convidados.

#  Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que mostre uma mensagem informando que você pode convidar apenas duas pessoas para o jantar.

#  Utilize pop() para remover os convidados de sua lista, um de cada vez, até que apenas dois nomes permaneçam em sua lista. Sempre que remover um nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela saiba que você sente muito por não poder convidá-la para o jantar.

# Apresente uma mensagem para cada uma das duas pessoas que continuam na lista, permitindo que elas saibam que ainda estão convidadas.

# Utilize del para remover os dois últimos nomes de sua lista, de modo que você tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem uma lista vazia no final de seu programa.

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
#print(dinner_wiht)

# inserir um novo convidado no meio da lista:

dinner_wiht.insert(2, 'Tata')
#print(dinner_wiht)

# inserir um novo convidado no final da lista 

dinner_wiht.append('Gustavo')
#print(dinner_wiht)

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

#print("\nE jantamos todos juntos.")

print("\nPorém infelizmente, não foi possível conseguir a mesa maior a tempo para o jantar. E, para piorar, só poderia levar 2 convidado. E informei o seguinte para os meus convidados: " + "\n\t'Pessoal, a mesa não estará disponível a tempo para o nosso jantar, e agora posso apenar levar 2 convidados. Me perdoem.'")

print(dinner_wiht)

#['Filomena', 'Jesus', 'Tata', 'Clarice', 'MEL', 'Gustavo']

#filó
popped_name_0 = dinner_wiht.pop(0)
print('\n' + popped_name_0 + ' nenê, ' + ' me desculpa, mas a juju te ve mais tarde.')

#tata
popped_name_1 = dinner_wiht.pop(1)
print('\n' + popped_name_1 +  ' me desculpa, mas a gente se encontra em londres.')

#mel
popped_name_2 = dinner_wiht.pop(2)
print('\n' + popped_name_2 +  ' me desculpa, meu nene, mas a gente se encontra em breve.')

#gustavo
popped_name_3 = dinner_wiht.pop(2)
print('\n' + popped_name_3 +  ' me desculpa, mas eu te encontro quando visitar a tata.')

print("\nSenhor " + dinner_wiht[0] + ", vamos jantar comigo?" )

print("\nVó " + dinner_wiht[1] + ", vamos jantar comigo?")

print(dinner_wiht)

#del

del dinner_wiht[0:2]

print(dinner_wiht)