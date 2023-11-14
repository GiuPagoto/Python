# REMOVENDO CARACTERES EM BRANCO DE NOMES: armazene o nome de uma pessoa e inclua alguns caracteres em branco no início e no final do nome. Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos uma vez.
# Exiba o nome uma vez, de modo que os espaços em branco em torno do nome sejam mostrados. Em seguida, exiba o nome usando cada uma das três funções de remoção de espaços: lstrip(), rstrip() e strip().

name = "\tGiullia\t\t\t\n\t\tPagoto\t"
#print(name)

# lstrip
print(name.lstrip())

# rstrip()
print(name.rstrip())

# strip()
print(name.strip())

name_2 = "\t\tGiullia\t\t\t"
print(name_2)

# lstrip
print(name_2.lstrip())

# rstrip()
print(name_2.rstrip())

# strip()
print(name_2.strip())
