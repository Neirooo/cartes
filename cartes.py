import random

#Définition de la classe joueur
class player():

    def __init__(self):
        self.name=()
        self.cards = []

    #changer le nom du joueur
    def setName(self, string):
        self.name = string
    
    #donner une carte au joueur
    def addCard(self, card):
        self.cards.append(card)

    #print proprement les data du joueur
    def prettyPrint(self):
        print(" NOM : "+self.name + " | NBCartes : "+str(len(self.cards)))
        print("CARTES : ", end="")
        text = ""
        for c in self.cards:
            text+=c+" | "
        text=text[:(len(text)-3)]
        print(text)
        print()
        


signes = ["p", "t", "c", "a"]
chiffres=["1","2","3","4","5","6","7","8","9","10","J","Q", "K"]
deck = []

[deck.append(a+b) for a in signes for b in chiffres] 
random.shuffle(deck)

listejoueurs = []



nbjoueur = 4

#de 0 à nbjoueur, créer un nouveau joueur, 
#lui donner un nom et l'ajouter à la liste de joueurs
for i in range(0, nbjoueur):
    tmppl = player()
    nom = "joueur"+str(i+1)
    tmppl.setName(nom)
    listejoueurs.append(tmppl)


#distribuer les cartes une à une
# n = 0 puis 1 puis 2 jusqu'à nbjoueur puis reviens à 0
# n représente l'index du joueur à qui on donne la carte
n=0
for i in range(0, len(deck)):
    pl = listejoueurs[n]
    pl.addCard(deck[i])
    n+=1
    if n==nbjoueur:
        n=0

#afficher les datas pour voir si tout marche correctement
for i in range(0, len(listejoueurs)):
    listejoueurs[i].prettyPrint()



