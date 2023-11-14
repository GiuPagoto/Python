cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# IGNORANDO AS DIFERENÇAS ENTRE LETRAS MAIÚSCULAS E MINÚSCULAS AO VERIFICAR A IGUALDADE

car = 'Audi'
print(car == 'audi') # false

car = 'Audi'
print(car.lower() == 'audi') # true

print(car) # Audi 


