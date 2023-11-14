# considere um parque de diversões que cobre preços distintos para grupos etários diferentes: 
# • a entrada para qualquer pessoa com menos de 4 anos é gratuita; 
# • a entrada para qualquer pessoa com idade entre 4 e 18 anos custa 5 dólares; 
# • a entrada para qualquer pessoa com 18 anos ou mais custa 10 dólares.


#1 

age = 20

if age < 4:
    print("entrada gratuita")

elif age >= 4 and age < 18:
    print("entrada: $5")

else:
    print("entrada: $10")

#2 

age = 20

if age < 4:
    print("Your admission cost is $0.")

elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# 3 (forma mais concisa)

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

# USANDO VÁRIOS BLOCOS ELIF
# se o parque de diversões implementasse um desconto para idosos, você poderia acrescentar mais um teste condicional no código a fim de determinar se uma pessoa está qualificada a receber esse desconto. Suponha que qualquer pessoa com 65 anos ou mais pague metade do preço normal da entrada, isto é, 5 dólares.

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print('Your admission cost is $' + str(price) + '.')

# OMITINDO O BLOCO ELSE
# Python não exige um bloco else no final de uma cadeia if-elif. Às vezes, um bloco else é útil; outras vezes, é mais claro usar uma instrução elif adicional que capture a condição específica de interesse.


age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >=65:
    price = 5

print('Your admission cost is $' + str(price) + '.')

# Se você tiver uma condição final específica para testar, considere usar um último bloco elif e omitir o bloco else.

