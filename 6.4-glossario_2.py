# GLOSSÁRIO 2:  Agora que você já sabe como percorrer um dicionário com um laço, limpe o código do Exercício 6.3 (página 148), substituindo sua sequência de instruções print por um laço que percorra as chaves e os valores do dicionário. Quando tiver certeza de que seu laço funciona, acrescente mais cinco termos de Python ao seu glossário. Ao executar seu programa novamente, essas palavras e significados novos deverão ser automaticamente incluídos na saída.

# 6.3

glossario = {
    'lista': 'Coleção ordenada de valores, separados por vírgula e dentro de colchetes, que são utilizadas para armazenar diversos itens em uma única variável.',
    'tupla': 'Estrutura de dados que funciona de modo semelhante a uma lista, entretanto, com a característica principal de ser imutável.',
    'laço': 'Utilizado para repetir uma parte do código por um conjunto de valores.',
    'teste condicional': 'É uma seção que ajuda a definir condições para a execução de determinados blocos de comandos.', 
    'dicionário': 'Coleção de dados em que se guarda uma chave e um valor correspondente.',
}


# Percorrer todos os pares chave-valor com um laço do dicinário

for palavra, significado_da_palavra in glossario.items(): 
    print(palavra.title() + 
          " : " + 
          significado_da_palavra + '\n\n') 