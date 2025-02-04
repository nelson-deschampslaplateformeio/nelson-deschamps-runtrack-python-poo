class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Accesseurs (Getters)
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs (Setters)
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def afficher_dimensions(self):
        print(f"Longueur : {self.__longueur}, Largeur : {self.__largeur}")



rect = Rectangle(10, 5)
rect.afficher_dimensions()


rect.set_longueur(15)
rect.set_largeur(8)


rect.afficher_dimensions()
