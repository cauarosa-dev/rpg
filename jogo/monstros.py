from random import randint
Selva_Esquecida = [
    {
        "nome" : "Slime_Verde",
        "vida" : 50,
        "dano" : 10,
        "nivel" : 1,
        "exp" : 15
    },
    {
        "nome" : "Globin_Saqueador",
        "vida" : 60,
        "dano" : 20,
        "nivel" : 2,
        "exp" : 30
    },
    {
        "nome" : "Lobo_Selvagem",
        "vida" : 60,
        "dano" : 20,
        "nivel" : 2,
        "exp" : 30
    },
    {
        "nome" : "Aranha_Venenosa",
        "vida" : 70,
        "dano" : 35,
        "nivel" : 3,
        "exp" : 47
    },
    {
        "nome" : "Org Renegado",
        "vida" : 75,
        "dano" : 43,
        "nivel" : 4,
        "exp" : 55
    },
    {
        "nome" : "Dragao_Anciao",
        "vida" : 100,
        "dano" : 50,
        "nivel" : 5,
        "exp" : 70
    }  
]
Carverna = [
    {
        "nome" : "Morcego",
        "vida" : 60,
        "dano" : 50,
        "nivel" : 6,
        "exp" : 2
    },
]


def escolher_monstro(boneco,lista):
    aleatorio_monstro = randint(0,5)
    aleatorio_monstro1 = randint(0,4)
    if boneco['nivel'] < 5:
        del lista[5]
        selva = lista[aleatorio_monstro1]
    elif boneco == 5:
        selva = lista[aleatorio_monstro]
    return selva
    

#def receber_dano(boneco,selva):
    #receber_dano = Selva_Esquecida[]

