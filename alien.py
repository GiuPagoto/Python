# Considere um jogo com alienígenas que possam ter cores e valores de pontuação diferentes. O dicionário simples a seguir armazena informações sobre um alienígena em particular:

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# TRABALHANDO COM DICIONÁRIOS
# Um dicionário em Python é uma coleção de pares chave-valor. Cada chave é conectada a um valor, e você pode usar uma chave para acessar o valor associado a ela. O valor de uma chave pode ser um número, uma string, uma lista ou até mesmo outro dicionário. De fato, podemos usar qualquer objeto que possa ser criado em Python como valor de um dicionário.

# ACESSANDO VALORES EM UM DICIONÁRIO
# Se um jogador atingir esse alienígena, podemos consultar quantos pontos ele deve ganhar usando um código como este:

new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')

# ADICIONANDO NOVOS PARES CHAVE-VALOR
# Dicionários são estruturas dinâmicas, e você pode adicionar novos pares chave-valor a um dicionário a qualquer momento. Por exemplo, para acrescentar um novo par chave-valor, especifique o nome do dicionário, seguido da nova chave entre colchetes, juntamente com o novo valor.
# Vamos adicionar duas novas informações ao dicionário alien_0: as coordenadas x e y do alienígena, que nos ajudarão a exibir o alienígena em determinada posição da tela. Vamos colocar o alienígena na borda esquerda da tela, 25 pixels abaixo da margem superior. Como as coordenadas da tela normalmente começam no canto superior esquerdo da tela, posicionaremos o alienígena na margem esquerda definindo coordenada x com 0, e 25 pixels abaixo da margem superior, definindo a coordenada y com o valor 25 positivo, como vemos aqui:

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# a ordem dos pares chave-valor não coincide com a ordem em que os adicionamos. Python não se importa com a ordem em que armazenamos cada par chave-valor; ele só se importa com a conexão entre cada chave e seu valor.

# COMEÇANDO COM UM DICIONÁRIO VAZIO
# Às vezes, é conveniente ou até mesmo necessário começar com um dicionário vazio e então acrescentar novos itens a ele. Para começar a preencher um dicionário vazio, defina-o com um conjunto de chaves vazio e depois acrescente cada par chave-valor em sua própria linha. Por exemplo, eis o modo de criar o dicionário alien_0 usando esta abordagem:

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5 

print(alien_0)

# Geralmente usamos dicionários vazios quando armazenamos dados fornecidos pelo usuário em um dicionário, ou quando escrevemos um código que gere um grande número de pares chave-valor automaticamente.

# MODIFICANDO VALORES EM UM DICIONÁRIO
# Para modificar um valor em um dicionário, especifique o nome do dicionário com a chave entre colchetes e o novo valor que você quer associar a essa chave. Por exemplo, considere um alienígena que muda de verde para amarelo à medida que o jogo prossegue:

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + '.')

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + '.')

# segundo exemplo: monitorar a posição de um alienígena que pode se deslocar com velocidades diferentes. Armazenaremos um valor que representa a velocidade atual do alienígena e, então, usaremos esse valor para determinar a distância que o alienígena deve se mover para a direita: 

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print(alien_0)

# mudar a velocidade
#alien_0['speed'] = 'fast'

print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1 
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3 

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

print(alien_0)

# REMOVENDO PARES CHAVE-VALOR
# instrução del para remover totalmente um par chave-valor.
# vamos remover a chave 'points' do dicionário alien_0, juntamente com seu valor: 

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# Saiba que o par chave-valor apagado é removido de forma permanente.

# UM DICIONÁRIO DE OBJETOS SEMELHANTES
# fazer uma enquete com várias pessoas e perguntar-lhes qual é a sua linguagem de programação favorita. Um dicionário é conveniente para armazenar os resultados de uma enquete simples, desta maneira: 

favorite_languages = {
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python',
                      }

print("Sarah´s favorite language is " + 
      favorite_languages['sarah'].title() + 
      '.')












