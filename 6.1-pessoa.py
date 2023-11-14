# PESSOA: : Use um dicionário para armazenar informações sobre uma pessoa que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a cidade em que ela vive. Você deverá ter chaves como first_name, last_name, age e city. Mostre cada informação armazenada em seu dicionário.

pessoa = {
    'nome': 'giullia',
    'sobrenome':'pagoto',
    'idade': '24',
    'cidade': 'catanduva',
}

print('O nome dessa menina é ' +
      pessoa['nome'].title() + ' ' +
      pessoa['sobrenome'].title() +
      '. Ela tem ' + pessoa['idade'] + ' '
      'anos, e mora em ' + 
      pessoa['cidade'].title() + 
      '.')


