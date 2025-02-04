class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}."

# Instanciation de plusieurs personnes avec des valeurs choisies
personne1 = Personne("Dupont", "Jean")
personne2 = Personne("Martin", "Sophie")
personne3 = Personne("Durand", "Paul")


print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())


def creer_personne():
    prenom = input("Entrez le prénom : ")
    nom = input("Entrez le nom : ")
    return Personne(nom, prenom)

# Création d'une personne avec des valeurs saisies par l'utilisateur
personne_utilisateur = creer_personne()
print(personne_utilisateur.SePresenter())