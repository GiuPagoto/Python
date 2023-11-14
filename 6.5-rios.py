# RIOS: : Crie um dicionário que contenha três rios importantes e o país que cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.

#  Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre pelo Egito.

rios = {
    'amazonas': 'brasil',
    'nilo': 'egito',
    'tejo': 'portugal',
}

for rio, pais in rios.items():
    print("O rio " + rio.title() + " corre pelo " + pais.title() + ".\n\n")

# Use um laço para exibir o nome de cada rio incluído no dicionário.

for rio in rios.keys():
    print("\n" + rio.title())


#  Use um laço para exibir o nome de cada país incluído no dicionário.

for pais in rios.values():
    print("\n" + pais.title())