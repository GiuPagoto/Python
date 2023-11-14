# COMPARAÇÕES NUMÉRICAS

# verifica se uma pessoa tem 18 anos:

age = 18
print(age == 18)

# testar se dois números não são iguais

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

# incluir também várias comparações matemáticas em suas instruções condicionais

age = 19

print(age < 21)
print(age<=21)
print(age > 21)
print(age >= 21)

# Testando várias condições
# testar várias condições ao mesmo tempo. Por exemplo, ocasionalmente, você pode precisar de duas condições True para executar uma ação. Em outros casos, poderia ficar satisfeito com apenas uma condição True. As palavras reservadas and e or podem ajudar nessas situações.

# Usando and para testar várias condições.
# Para verificar se duas condições são True simultaneamente, utilize a palavra reservada and para combinar os dois testes condicionais; se cada um dos testes passar, a expressão como um todo será avaliada como True. Se um dos testes falhar, ou ambos, a expressão será avaliada como False.

# verificar se duas pessoas têm mais de 21 anos usando o teste a seguir:

age_0 = 22
age_1 = 18

print(age_0 >= 21 and age_1 >= 21) # False

age_1 = 22
print(age_0 >= 21 and age_1 >= 21) # True 

# melhorar a legibilidade 

print((age_0 >= 21) and (age_1 >= 21)) # False

# USANDO OR PARA TESTAR VÁRIAS CONDIÇÕES
# o teste passa se um dos testes individuais passar, ou ambos.
# Uma expressão or falha somente quando os dois testes individuais falharem.
# Vamos considerar duas idades novamente, porém, desta vez, queremos que apenas uma das pessoas tenha mais de 21 anos: 

age_0 = 22
age_1 = 18

print(age_0 >=21 or age_1 >= 21) # True

age_0 = 18
print(age_0 >= 21 or age_1 >= 21) # False





















