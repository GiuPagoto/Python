# MAIS TESTES CONDICIONAIS: Você não precisa limitar o número de testes que criar em dez. Se quiser testar mais comparações. Tenha pelo menos um resultado True e um False para cada um dos casos a seguir:

#  testes de igualdade e de não igualdade com strings;

city = 'Fortaleza'
print("city == " + city)

print("\nIs city == 'São Paulo'?")
print(city == 'São Paulo')

#  testes usando a função lower()

print("\nIs city == 'fortaleza'?")
print(city.lower() == 'fortaleza')

# testes numéricos que envolvam igualdade e não igualdade, maior e menor que, maior ou igual a e menor ou igual a

soma = 5 + 9
print("soma == " + str(soma))

# igualdade

print("\nsoma == 14?")
print(soma == 14) # TRUE

print("\nsoma == 15?")
print(soma == 15) # FALSE

# não igualdade

print("\nsoma != 20?")
print(soma != 20) # TRUE

print("\nsoma != 14?")
print(soma != 14) # FALSE

# maior e menor que (e and)

print("\nsoma>10 and soma<20?")
print(soma>10 and soma<20) # TRUE

print("\nsoma>14 and soma<20?") 
print(soma>14 and soma<20) # FALSE
#Se um dos testes falhar, ou ambos, a expressão será avaliada como False.

# maior ou igual a e menor ou igual a (e and)

print("\nsoma>=15 and soma=<20?")
print(soma>=15 and soma<=20) # FALSE
#Se um dos testes falhar, ou ambos, a expressão será avaliada como False.

print("\nsoma>=14 and soma=<20?") 
print(soma>=14 and soma<=20) # TRUE

# maior e menor que (e or)

print("\nsoma>10 or soma<20?")
print(soma>10 or soma<20) # TRUE

print("\nsoma>15 or soma<9?") 
print(soma>15 or soma<9) # FALSE
#Uma expressão or falha somente quando os dois testes individuais falharem

# maior ou igual a e menor ou igual a (e and)

print("\nsoma>=15 or soma=<9?")
print(soma>=15 or soma<=9) # FALSE
#Uma expressão or falha somente quando os dois testes individuais falharem

print("\nsoma>=24 or soma=<20?") 
print(soma>=24 or soma<=20) # TRUE

# testes para verificar se um item está em uma lista

numbers = list(range(1,31))
print("numbers: ")
print(numbers)

print("\nIs soma in numbers?")
print(soma in numbers) #true

numbers = list(range(0,13))
print("numbers: ")
print(numbers)

print("\nIs soma in numbers?")
print(soma in numbers) #false

# testes para verificar se um item não está em uma lista.

numbers = list(range(0,31))
print("numbers: ")
print(numbers)

print("\nIs soma not in numbers?")
print(soma not in numbers) #false

numbers = list(range(0,13))
print("numbers: ")
print(numbers)

print("\nIs soma not in numbers?")
print(soma not in numbers) #true


