import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
    
    def est_vivant(self):
        return self.vie > 0
    
    def afficher_vie(self):
        print(f"{self.nom} a {self.vie} points de vie restants.")

class Jeu:
    def __init__(self):
        self.niveau = None
    
    def choisirNiveau(self):
        print("Choisissez un niveau de difficulté: 1. Facile  2. Moyen  3. Difficile")
        choix = input("Entrez le numéro du niveau: ")
        if choix == "1":
            self.niveau = "Facile"
            joueur_vie, ennemi_vie = 100, 80
        elif choix == "2":
            self.niveau = "Moyen"
            joueur_vie, ennemi_vie = 80, 80
        else:
            self.niveau = "Difficile"
            joueur_vie, ennemi_vie = 80, 100
        
        return joueur_vie, ennemi_vie
    
    def lancerJeu(self):
        joueur_vie, ennemi_vie = self.choisirNiveau()
        joueur = Personnage("Joueur", joueur_vie)
        ennemi = Personnage("Ennemi", ennemi_vie)
        
        print(f"Début du combat ! Niveau: {self.niveau}")
        
        while joueur.est_vivant() and ennemi.est_vivant():
            joueur.attaquer(ennemi)
            if ennemi.est_vivant():
                ennemi.attaquer(joueur)
            joueur.afficher_vie()
            ennemi.afficher_vie()
            print("-")
        
        self.verifierVainqueur(joueur, ennemi)
    
    def verifierVainqueur(self, joueur, ennemi):
        if joueur.est_vivant():
            print("Félicitations ! Vous avez gagné !")
        else:
            print("Dommage... L'ennemi a gagné.")

# Lancer le jeu
jeu = Jeu()
jeu.lancerJeu()
