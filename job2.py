class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print(f"Âge: {self.age} ans")
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        print(f"J’ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=14):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer")

# Instanciation
personne = Personne()
eleve = Eleve()
professeur = Professeur("Maths", 40)

# Modification et affichage de l'âge de l'élève
eleve.modifierAge(15)
eleve.afficherAge()

# Actions de l'élève
eleve.bonjour()
eleve.allerEnCours()

# Actions du professeur
professeur.bonjour()
professeur.enseigner()
