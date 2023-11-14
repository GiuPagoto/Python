# FATIAS: Usando um dos programas que você escreveu neste capítulo, acrescente várias linhas no final do programa que façam o seguinte:
# • Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para exibir os três primeiros itens da lista desse programa.




##########################ERRADO############################

#lista = list(range(1,11))
#cubos = []

#for numero in lista:
    #cubo = numero**3 
    #cubos.append(cubo)

#print(cubo)

##############################################################

#################4.8-cubos####################################

#cubos = list(range(1,11))

#for cubo in cubos:
   #print(cubo**3)

##############################################################

cubos = []

for value in range(1,11):
    cubos.append(value**3) # Cada valor do laço é elevado ao cubo e, então, é imediatamente concatenado à lista de cubos.

print(cubos)

print("Os três primeiros números da lista são: ")

for cubo in cubos[:3]:
   print(cubo)

# • Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três itens do meio da lista.

print("Os trê números do meio da lista são: ")

for cubo in cubos[4:7]:
    print(cubo)

# • Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir os três últimos itens da lista.

print("Os três últimos itens da lista são: ")

for cubo in cubos[-3:]:
    print(cubo)




