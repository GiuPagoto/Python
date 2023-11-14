# CRIANDO LISTAS NUMÉRICAS

# Há muitos motivos para armazenar um conjunto de números. Por exemplo, você precisará manter um controle das posições de cada personagem em um jogo, e talvez queira manter um registro das pontuações mais altas de um jogador também. Em visualizações de dados, quase sempre você trabalhará com conjuntos de números, como temperaturas, distâncias, tamanhos de população ou valores de latitudes e longitudes, entre outros tipos de conjuntos numéricos.

# As listas são ideais para armazenar conjuntos de números, e Python oferece várias ferramentas para ajudar você a trabalhar com listas de números de forma eficiente. Depois que souber usar efetivamente essas ferramentas, seu código funcionará bem, mesmo quando suas listas tiverem milhões de itens.

#  FUNÇÃO range()

for value in range(1,5): # 1 2 3 4
    print(value)  

for value in range(1,6): # 1 2 3 4 5 
    print(value)

# USANDO range() para criar uma lista de números
# Se quiser criar uma lista de números, você pode converter os resultados de range() diretamente em uma lista usando a função list(). Quando colocamos list() em torno de uma chamada à função range(), a saída será uma lista de números.

numbers = list(range(1,6))
print(numbers)


