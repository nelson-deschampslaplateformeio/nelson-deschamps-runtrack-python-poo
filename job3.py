class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "À faire"
    
    def marquerCommeFinie(self):
        self.statut = "Terminée"
    
    def __str__(self):
        return f"{self.titre} - {self.description} [{self.statut}]"

class ListeDeTaches:
    def __init__(self):
        self.taches = []
    
    def ajouterTache(self, tache):
        self.taches.append(tache)
    
    def supprimerTache(self, titre):
        self.taches = [tache for tache in self.taches if tache.titre != titre]
    
    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.marquerCommeFinie()
    
    def afficherListe(self):
        return [str(tache) for tache in self.taches]
    
    def filterListe(self, statut):
        return [str(tache) for tache in self.taches if tache.statut == statut]

# Création de la liste de tâches
liste = ListeDeTaches()

# Création de tâches
tache1 = Tache("regarder les musiques", "écouter les musiques de la semaine")
tache2 = Tache("Réviser Python", "Pratiquer les classes et objets")
tache3 = Tache("continuer la lecture", "réprendre le livre au chapitre actuel")

# Ajout des tâches à la liste
liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

# Marquer une tâche comme terminée
liste.marquerCommeFinie("écouter les musiques de la semaine")

# Supprimer une tâche
liste.supprimerTache("réprendre le livre au chapitre actuel")

# Afficher toutes les tâches
print("Toutes les tâches:", liste.afficherListe())

# Afficher uniquement les tâches à faire
print("Tâches à faire:", liste.filterListe("À faire"))
