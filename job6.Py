class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

# Instanciation de l'objet Animal
animal = Animal()


print("L'âge de l'animal :", animal.age ,"ans")


animal.vieillir()
print("L'âge de l'animal en vieillissant:", animal.age, "ans")


animal.nommer("opale")
print("L'animal se nomme :", animal.prenom)
