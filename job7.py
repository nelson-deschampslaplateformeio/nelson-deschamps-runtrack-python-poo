class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def gauche(self, valeur):
        self.x -= valeur

    def droite(self, valeur):
        self.x += valeur

    def haut(self, valeur):
        self.y -= valeur

    def bas(self, valeur):
        self.y += valeur

    def position(self):
        return (self.x, self.y)

# Instanciation du personnage
personnage = Personnage()


print("Position initiale :", personnage.position())

dep_gauche = int(input("Entrez la valeur pour aller à gauche : "))
dep_droite = int(input("Entrez la valeur pour aller à droite : "))
dep_haut = int(input("Entrez la valeur pour aller en haut : "))
dep_bas = int(input("Entrez la valeur pour aller en bas : "))


personnage.gauche(dep_gauche)
personnage.droite(dep_droite)
personnage.haut(dep_haut)
personnage.bas(dep_bas)

print("Nouvelle position :", personnage.position())