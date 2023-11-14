# ALTERANDO A LISTA DE CONVIDADOS: Você acabou de saber que um de seus convidados não poderá comparecer ao jantar, portanto será necessário enviar um novo conjunto de convites. Você deverá pensar em outra pessoa para convidar.

# Comece com seu programa do Exercício 3.4. Acrescente uma instrução print no final de seu programa, especificando o nome do convidado que não poderá comparecer.

# Modifique sua lista, substituindo o nome do convidado que não poderá comparecer pelo nome da nova pessoa que você está convidando.

# Exiba um segundo conjunto de mensagens com o convite, uma para cada pessoa que continua presente em sua lista.

dinner_wiht = ['Jesus', 'Clarice' ,'Alex Turner']

mensagem = "Quero muito conhecer o Senhor " + dinner_wiht[0].upper() + " e compreender a sua existência. Por isso, te convido para um jantar."
print(mensagem)

mensagem = "Queria muito matar a saudade da Dona " + dinner_wiht[1].upper() + ". E aproveitar um jantar com ela."
print(mensagem)

mensagem = "Queria muito ver o  " + dinner_wiht[2].upper() + " tocando em um show e depois sair para jantar com ele."
print(mensagem)

print("\nPorém, o " + dinner_wiht[2].upper() + ' não poderá comparecer, porque bebeu muito.')

# modificando elementos de uma lista
dinner_wiht[2] = 'MEL'
print(dinner_wiht)

print("Mas, felizmente, eu reencontrei a " + dinner_wiht[2] + ' que é uma companhia 1000 vezes melhor. Assim, eu a convidei para jantar.')

print("E, nesse jantar, minha vó " + dinner_wiht[1] + " também estava presente.")

print("E, o meus Senhor " + dinner_wiht[0] + " também. Por isso, estou muito feliz.")