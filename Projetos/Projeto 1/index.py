import json
file = open('data.json', "wb")
def questions():    
    pergunta1 = input("Nome: ")
    pergunta2 = int(input("Idade: "))
    pergunta3 = input("Endereço: ")
    lista = [pergunta1, pergunta2, pergunta3]
    data_strings = json.dumps(lista)
    data_strings
    file.write(data_strings.encode())
    file.close
questions()