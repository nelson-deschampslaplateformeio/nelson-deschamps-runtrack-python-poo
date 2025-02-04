class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Valeur de x : {self.x}")

    def afficherY(self):
        print(f"Valeur de y : {self.y}")

    def changerX(self, new_x):
        self.x = new_x

    def changerY(self, new_y):
        self.y = new_y


def creer_point():
    x = int(input("Entrez la coordonnée x : "))
    y = int(input("Entrez la coordonnée y : "))
    return Point(x, y)

# Instanciation d'un point avec les valeurs saisies par l'utilisateur
point = creer_point()


point.afficherLesPoints()


point.afficherX()
point.afficherY()

point.changerX(10)
point.changerY(15)

point.afficherLesPoints()
