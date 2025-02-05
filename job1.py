class Ville:
    def __init__(self, nom, population):
        self.__nom = nom
        self.__population = population
    
    def ajouter_habitant(self):
        self.__population += 1
    
    def get_population(self):
        return self.__population
    
    def get_nom(self):
        return self.__nom

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouter_population()
    
    def ajouter_population(self):
        self.__ville.ajouter_habitant()

# Création des villes
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage initial
print(f"Population initiale de {paris.get_nom()} : {paris.get_population()}")
print(f"Population initiale de {marseille.get_nom()} : {marseille.get_population()}")

# Création des personnes
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Affichage après ajout des habitants
print(f"Population de {paris.get_nom()} après l'arrivée de nouveaux habitants : {paris.get_population()}")
print(f"Population de {marseille.get_nom()} après l'arrivée de nouveaux habitants : {marseille.get_population()}")
