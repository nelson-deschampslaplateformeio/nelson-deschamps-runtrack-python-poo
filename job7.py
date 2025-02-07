import random

# Classe Carte
class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"
    
    def get_valeur(self):
        # Les figures (J, Q, K) valent 10 points
        if self.valeur in ['J', 'Q', 'K']:
            return 10
        # L'As peut valoir 1 ou 11
        elif self.valeur == 'A':
            return 11
        else:
            return int(self.valeur)

# Classe Jeu
class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()
        self.joueur_main = []
        self.croupier_main = []
        
    def creer_paquet(self):
        # Création d'un paquet de 52 cartes
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        paquet = [Carte(valeur, couleur) for couleur in couleurs for valeur in valeurs]
        random.shuffle(paquet)  # Mélange le paquet
        return paquet
    
    def distribuer(self):
        # Distribuer 2 cartes à chaque joueur et au croupier
        self.joueur_main = [self.paquet.pop(), self.paquet.pop()]
        self.croupier_main = [self.paquet.pop(), self.paquet.pop()]
    
    def calculer_points(self, main):
        points = sum(carte.get_valeur() for carte in main)
        as_count = sum(1 for carte in main if carte.valeur == 'A')
        
        # Si l'As est présent et que le total des points dépasse 21, on ajuste la valeur de l'As à 1
        while points > 21 and as_count:
            points -= 10
            as_count -= 1
        return points
    
    def afficher_main(self, joueur):
        # Affiche la main du joueur ou du croupier
        if joueur == 'joueur':
            print("Main du joueur:", ', '.join(str(carte) for carte in self.joueur_main))
        elif joueur == 'croupier':
            print("Main du croupier:", ', '.join(str(carte) for carte in self.croupier_main))
    
    def tour_joueur(self):
        # Le joueur choisit de prendre des cartes ou de passer
        while True:
            self.afficher_main('joueur')
            points = self.calculer_points(self.joueur_main)
            print(f"Points du joueur: {points}")
            if points > 21:
                print("Le joueur a dépassé 21, il perd !")
                return False  # Le joueur a perdu
            action = input("Voulez-vous 'prendre' une carte ou 'passer' ? ").lower()
            if action == 'prendre':
                self.joueur_main.append(self.paquet.pop())
            elif action == 'passer':
                break
            else:
                print("Option invalide. Tapez 'prendre' ou 'passer'.")
        return True
    
    def tour_croupier(self):
        # Le croupier prend des cartes jusqu'à avoir au moins 17 points
        while self.calculer_points(self.croupier_main) < 17:
            self.croupier_main.append(self.paquet.pop())
        self.afficher_main('croupier')
        points = self.calculer_points(self.croupier_main)
        print(f"Points du croupier: {points}")
        return points
    
    def jouer(self):
        # Démarre une partie de Blackjack
        self.distribuer()
        if not self.tour_joueur():
            return "Le joueur a perdu."
        points_croupier = self.tour_croupier()
        points_joueur = self.calculer_points(self.joueur_main)
        
        # Décision du gagnant
        if points_croupier > 21 or points_joueur > points_croupier:
            return "Le joueur gagne !"
        elif points_joueur == points_croupier:
            return "Match nul !"
        else:
            return "Le croupier gagne !"

# Lancement du jeu
jeu = Jeu()
resultat = jeu.jouer()
print(resultat)
