class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f"Produit : {self.nom}\nPrix HT : {self.prixHT}€\nTVA : {self.TVA}%\nPrix TTC : {self.calculerPrixTTC():.2f}€"

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

    def getPrixTTC(self):
        return self.calculerPrixTTC()


# Création de plusieurs produits
produit1 = Produit("Ordinateur portable", 1000, 20)
produit2 = Produit("Smartphone", 800, 20)
produit3 = Produit("Chaise de bureau", 150, 5)


print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

produit1.modifierNom("Ordinateur portable Gamer")
produit1.modifierPrix(1200)

produit2.modifierNom("Smartphone Ultra")
produit2.modifierPrix(850)

produit3.modifierNom("Chaise ergonomique")
produit3.modifierPrix(200)

print("\nAprès modification des produits :")
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())
