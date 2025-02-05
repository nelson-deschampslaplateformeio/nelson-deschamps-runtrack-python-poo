class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0
    
    def marquerUnBut(self):
        self.buts += 1
    
    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
    
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
    
    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
    
    def afficherStatistiques(self):
        return f"{self.nom} (#{self.numero}, {self.position}) - Buts: {self.buts}, Passes décisives: {self.passes_decisives}, Jaunes: {self.cartons_jaunes}, Rouges: {self.cartons_rouges}"

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
    
    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
    
    def afficherStatistiquesJoueurs(self):
        for joueur in self.joueurs:
            print(joueur.afficherStatistiques())
    
    def mettreAJourStatistiquesJoueur(self, numero, action):
        for joueur in self.joueurs:
            if joueur.numero == numero:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()

# Création des équipes
equipe1 = Equipe("Les Aigles")
equipe2 = Equipe("Les Lions")

# Création des joueurs
joueur1 = Joueur("Paul Pogba", 6, "Milieu")
joueur2 = Joueur("Kylian Mbappé", 10, "Attaquant")
joueur3 = Joueur("Hugo Lloris", 1, "Gardien")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)

# Affichage initial des statistiques
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

# Simulation d'un match
equipe1.mettreAJourStatistiquesJoueur(10, "but")
equipe1.mettreAJourStatistiquesJoueur(6, "passe")
equipe2.mettreAJourStatistiquesJoueur(1, "jaune")

# Affichage après le match
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
