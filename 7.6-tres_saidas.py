""" 

Três saídas: 

Escreva versões diferentes do Exercício 7.4 ou do Exercício
7.5 que faça o seguinte, pelo menos uma vez: 

• use um teste condicional na instrução while para encerrar o laço; 
• use uma variável active para controlar o tempo que o laço executará; 
• use uma instrução break para sair do laço quando o usuário fornecer o valor 'quit'.

"""

# use um teste condicional na instrução while para encerrar o laço; 

prompt = "\nInforme a sua idade para saber o valor do ingresso: "

while True:
    idade = input(prompt)

    idade = int(idade)

    if idade < 3:
        print('O seu ingresso é gratuito!')
    
    elif idade >= 3 and idade <= 12:
        print('O seu ingresso custará $10.')

    else:
        print('O seu ingresso custará $15.')