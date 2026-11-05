
nome = input("Digite o nome do personagem: ")

personagem = { 
        "nome" : nome,
        "vida" : 100,
        "dano" : 5,
        "mana" : 50,
        "nivel" : 1,
        "experiencia" : 0
    }
def mostrar_status(lista):
    for status, statu in lista.items():
        if status == 'nome':
            continue
        else:
            print(f"{status} : {statu}")

#def ganhar_xp(personagem,selva):
    
     
def level_up(personagem):
    if personagem['experiencia'] >= 100:
        personagem['experiencia'] = 0
        personagem['nivel'] += 1
        personagem['vida'] += 75
        personagem['dano'] += 10
        personagem['mana'] += 50
    return personagem

def receber_dano(personagem,selva):
    receber_dano = personagem['vida'] - selva['dano']
    personagem['vida'] = receber_dano
    if personagem['vida'] == 0:
        print("Morrel")
        return
    return personagem

