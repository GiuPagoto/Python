# CORES DE ALIENÍGENAS: Transforme sua cadeia if-else do Exercício 5.4 em uma cadeia if-elif-else.

# Se o alienígena for verde, mostre uma mensagem informando que o jogador ganhou cinco pontos.

# Se o alienígena for amarelo, mostre uma mensagem informando que o jogador ganhou dez pontos.

# Se o alienígena for vermelho, mostre uma mensagem informando que o jogador ganhou quinze pontos.

# Escreva três versões desse programa, garantindo que cada mensagem seja exibida para a cor apropriada do alienígena.

# 1

alien_color = 'green'

if alien_color == 'green':
    print("Parabéns! Você acabou de ganhar 5 pontos!")
elif alien_color  == 'yellow':
    print("Parabéns! Você acabou de ganhar 10 pontos!")
else:
    print("Parabéns! Você acabou de ganhar 15 pontos!")

# 2

alien_color = 'yellow'

if alien_color == 'green':
    print("Parabéns! Você acabou de ganhar 5 pontos!")
elif alien_color  == 'yellow':
    print("Parabéns! Você acabou de ganhar 10 pontos!")
else:
    print("Parabéns! Você acabou de ganhar 15 pontos!")

# 3

alien_color = 'red'

if alien_color == 'green':
    print("Parabéns! Você acabou de ganhar 5 pontos!")
elif alien_color  == 'yellow':
    print("Parabéns! Você acabou de ganhar 10 pontos!")
else:
    print("Parabéns! Você acabou de ganhar 15 pontos!")