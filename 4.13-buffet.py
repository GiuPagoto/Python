# BUFFET: Um restaurante do tipo buffet oferece apenas cinco tipos básicos de comida. Pense em cinco pratos simples e armazene-os em uma tupla.

buffet = ('lasanha', 'macarrão', 'pizza', 'hamburguer', 'batata')

# • Use um laço for para exibir cada prato oferecido pelo restaurante.

for prato in buffet:
    print(prato)

# • Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.

# buffet[3] = 'feijão'

#  O restaurante muda seu cardápio, substituindo dois dos itens com pratos diferentes. Acrescente um bloco de código que reescreva a tupla e, em seguida, use um laço for para exibir cada um dos itens do cardápio revisado.

#buffet_novo = buffet[:] PODE COPIAR
#print(buffet)

# buffet_novo.append("feijão",'ovo mexido') NÃO PODE ACRESCENTAR ITENS NOVOS 
# print(buffet_novo)

buffet_novo = ('lasanha', 'macarrão', 'batata', 'feijão', 'ovo mexido')

for comida in buffet_novo:
    print(comida)
