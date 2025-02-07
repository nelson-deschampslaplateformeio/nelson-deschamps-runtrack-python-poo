class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def volume(self):
        return self.surface() * self.__hauteur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

# Instanciation et tests
rectangle = Rectangle(10, 5)
print(f"Périmètre du rectangle: {rectangle.perimetre()}")
print(f"Surface du rectangle: {rectangle.surface()}")

# Instanciation et test du parallélépipède
parallelepipede = Parallelepipede(10, 5, 8)
print(f"Volume du parallélépipède: {parallelepipede.volume()}")
