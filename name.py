# MÉTODOS

name = "giullia pagoto"

# Método title(): exibe cada palavra com uma letra maiúscula no início
print(name.title())
# Giullia Pagoto

#Método upper():
print(name.upper())
# GIULLIA PAGOTO

#Método lower(): útil para armazenar dados e depois exibir da forma mais conveniente
print(name.lower())
# giullia pagoto


# CONCATENANDO STRINGS

first_name = "giullia"
last_name = "pagoto"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!"  )

message = "Hello, " + full_name.title() + "!"
print(message)

# ACRESCENTANDO ESPAÇOS EM BRANCO EM STRINGS COM TABULAÇÕES OU QUEBRAS DE LINHA 

# tabulação:
print("Python")
print("\tPython") #tab
print("Languages:\n\tPython\n\tC\n\tJavaScript") #pula linha e tab

# REMOVENDO ESPAÇOS EM BRANCO: importante para comparar duas strings

# funções de remoção são usadas com mais frequência para limpar entradas de usuário antes de armazená-kas em um programa (???)

favorite_language = "python "
print(favorite_language)

print(favorite_language.rstrip()) # tira, temporariamente, o espaço em branco que está a direita 

favorite_language = favorite_language.rstrip()
print(favorite_language) # tira permanentemente o espaço em branco que está a direita 

favorite_language = " python "
print(favorite_language)
print(favorite_language.lstrip()) # tira, temporariamente, o espaço em branco que está a esquerda
print(favorite_language.strip()) # tira os espaços em branco dos dois lados 


