import math

class Cercle:
    def __init__(self, rayon):
        # Initialisation du rayon du cercle
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Cercle de rayon : {self.rayon}")
        print(f"Diamètre : {self.diametre()}")
        print(f"Circonférence : {self.circonference():.2f}")
        print(f"Aire : {self.aire():.2f}")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon

cercle1 = Cercle(4)
cercle2 = Cercle(7)

print("Informations du premier cercle :")
cercle1.afficherInfos()
print("\nInformations du deuxième cercle :")
cercle2.afficherInfos()
