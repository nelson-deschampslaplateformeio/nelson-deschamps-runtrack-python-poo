import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
    
    def aire(self):
        return math.pi * (self.radius ** 2)

class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    
    def informationsVehicule(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}, Prix: {self.prix}")
    
    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")
    
    def demarrer(self):
        print("La voiture démarre en douceur!")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")
    
    def demarrer(self):
        print("La moto vrombit et démarre!")

# Instanciation et test du rectangle
rectangle = Rectangle(10, 5)
print(f"Aire du rectangle: {rectangle.aire()}")

# Instanciation et test du cercle
cercle = Cercle(7)
print(f"Aire du cercle: {cercle.aire()}")

# Instanciation et test de la voiture
voiture = Voiture("Toyota", "Corolla", 2022, 20000)
voiture.informationsVehicule()
voiture.demarrer()

# Instanciation et test de la moto
moto = Moto("Honda", "CBR", 2023, 15000)
moto.informationsVehicule()
moto.demarrer()
