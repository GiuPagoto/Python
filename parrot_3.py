'''

Para um programa que deva executar somente enquanto muitas
condições forem verdadeiras, podemos definir uma variável que
determina se o programa como um todo deve estar ativo. Essa variável, chamada de flag, atua como um sinal para o programa. Podemos escrever nossos programas de modo que executem enquanto a flag estiver definida com True e parem de executar quando qualquer um dos vários eventos definir o valor da flag com False. Como resultado, nossa instrução while geral precisa verificar apenas uma condição: se a flag, no momento, é True. Então todos os nossos demais testes (para ver se um evento que deve definir a flag com False ocorreu) podem estar bem organizados no restante do programa.

Vamos adicionar uma flag em parrot.py.

Essa flag, que chamaremos de active (embora você possa lhe dar o nome que quiser), controlará se o programa deve ou não continuar executando.

'''

prompt = "\nTell me something, and I will repeat it back to you: "

prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


