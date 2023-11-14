# ENQUETE: Utilize o código em favorite_languages.py
#  Crie uma lista de pessoas que devam participar da enquete sobre linguagem favorita. Inclua alguns nomes que já estejam no dicionário e outros que não estão.
# Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem respondido à enquete, mostre uma mensagem agradecendo-lhes por responder. Se ainda não participaram da enquete, apresente uma mensagem convidando-as a responder.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

pessoas = ['sarah', 'phil', 'giullia', 'filo']
     
for name in pessoas:
    if name in favorite_languages.keys():
        print("\nOlá, " + name.title() + 
              "! Obrigada por ter participado da nossa enquete.") 
    else:
        print("\nOlá, " + name.title() + 
              "! Participe da nossa enquete.") 
    


