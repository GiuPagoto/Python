# PERCORRENDO UMA LISTA INTEIRA COM UM LAÇO

# Com frequência, você vai querer percorrer todas as entradas de uma lista, executando a mesma tarefa em cada item. Por exemplo, em um jogo, você pode mover todos os elementos da tela de acordo com a mesma distância; em uma lista de números, talvez você queira executar a mesma operação estatística em todos os elementos. Quem sabe você queira exibir cada um dos títulos de uma lista de artigos em um site. Quando quiser executar a mesma ação em todos os itens de uma lista, você pode usar o laço for de Python.

# Vamos supor que temos uma lista de nomes de mágicos e queremos exibir todos os nomes da lista. Poderíamos fazer isso recuperando cada nome da lista individualmente, mas essa abordagem poderia causar vários problemas. Para começar, seria repetitivo fazer isso com uma lista longa de nomes. Além disso, teríamos que alterar o nosso código sempre que o tamanho da lista mudasse. Um laço for evita esses dois problemas ao permitir que Python administre essas questões internamente.

# Vamos usar um laço for para exibir cada um dos nomes de uma lista de mágicos:

# lista
magicians = ['alice', 'david', 'carolina']

# laço for 
for magician in magicians: # Essa linha diz a Python para extrair um nome da lista magicians e armazená-lo na variável magician.
    print(magician + "\n") # exibir o nome que acabou de ser armazenado em magician.

# O interpretador então repete as linhas 13 e 14, uma vez para cada nome da lista.

# Executando mais tarefas em um laço for

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician.title() + ', that was a great trick!\n')



magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician.title() + ', that was a great trick!')
    print("I can´t wait to see your next trick, " + magician.upper() + ".\n")

# Fazendo algo após um laço for
# Vamos escrever um agradecimento ao grupo de mágicos como um todo, agradecendo-lhes por apresentar um show excelente.

print("Thank you, everyone. That was a great magician show!")

# Quando processar dados com um laço for, você verá que essa é uma boa maneira de sintetizar uma operação realizada em todo um conjunto de dados. Por exemplo, um laço for pode ser usado para inicializar um jogo percorrendo uma lista de personagens e exibindo cada um deles na tela. Você pode então escrever um bloco não indentado após esse laço, que exiba um botão Play Now (Jogue agora) depois que todos os personagens tiverem sido desenhados na tela.






