# GLOSSÁRIO: Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para evitar confusão, vamos chamá-lo de glossário.
# Pense em cinco palavras relacionadas à programação que você conheceu nos capítulos anteriores. Use essas palavras como chaves em seu glossário e armazene seus significados como valores.
#  Mostre cada palavra e seu significado em uma saída formatada de modo elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu significado, ou apresentar a palavra em uma linha e então exibir seu significado indentado em uma segunda linha. Utilize o caractere de quebra de linha (\n) para inserir uma linha em branco entre cada par palavra significado em sua saída.

glossario = {
    'lista': 'Coleção ordenada de valores, separados por vírgula e dentro de colchetes, que são utilizadas para armazenar diversos itens em uma única variável.',
    'tupla': 'Estrutura de dados que funciona de modo semelhante a uma lista, entretanto, com a característica principal de ser imutável.',
    'laço': 'Utilizado para repetir uma parte do código por um conjunto de valores.',
    'teste condicional': 'É uma seção que ajuda a definir condições para a execução de determinados blocos de comandos.', 
    'dicionário': 'Coleção de dados em que se guarda uma chave e um valor correspondente.',
}


print('Lista: ' + glossario['lista'] + '\n\n' +
      'Tupla: ' + glossario['tupla'] + '\n\n' + 
      'Laço: ' + glossario['laço'] + '\n\n' + 
      'Teste condicional: ' + glossario['teste condicional'] + '\n\n' + 
      'Dicionário: ' + glossario['dicionário'])