# CONHECENDO O MUNDO: Pense em pelo menos cinco lugares do mundo quevocê gostaria de visitar.

# Egito, Monte Carlo, Sicília, Grécia, Los Angeles

# Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em ordem alfabética.

viagens = ['Egito', 'Monte Carlo', 'Sicília', 'Grécia', 'Los Angeles']

# Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma elegante; basta exibi-la como uma lista Python pura.

print(viagens)

# Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista propriamente dita.

print(sorted(viagens))

# Mostre que sua lista manteve sua ordem original exibindo-a.

print(viagens)

# Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a ordem da lista original.

print(sorted(viagens, reverse = True))

# Mostre que sua lista manteve sua ordem original exibindo-a novamente.

print(viagens)

#  Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar que sua ordem mudou

viagens.reverse()
print(viagens)

# Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para mostrar que ela voltou à sua ordem original.

viagens.reverse()
print(viagens)

# Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.

# ordem_alfabetica = viagens.sort()

#viagens = ['Egito', 'Monte Carlo', 'Sicília', 'Grécia', 'Los Angeles']

#ordem_alfabetica = viagens.sort()
#print(ordem_alfabetica)

viagens.sort()
print(viagens)

# Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.

viagens.sort(reverse = True)
print(viagens)



