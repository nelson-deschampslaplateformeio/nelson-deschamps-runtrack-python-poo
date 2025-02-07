class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur

# Instanciation et test du rectangle
rectangle = Rectangle(10, 5)
print(f"Aire du rectangle: {rectangle.aire()}")