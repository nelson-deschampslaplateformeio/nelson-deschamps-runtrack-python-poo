from abc import ABC

class Commande(ABC):
    def __init__(self, numéro: int):
        self.__numéro = numéro
        self.__plats = {} 
        self.__statut = "En cours"
    
   
    def ajouter_plat(self, nom: str, prix: float):
        if prix > 0:
            self.__plats[nom] = prix
            print(f"Plat {nom} ajouté à la commande.")
        else:
            print("Le prix du plat doit être positif.")
   
    def annuler_commande(self):
        self.__statut = "Annulée"
        print("Commande annulée.")
    
    def terminer_commande(self):
        self.__statut = "Terminée"
        print("Commande terminée.")

    def __calculer_total(self):
        return sum(self.__plats.values())
    
    
    def calculer_tva(self, taux: float = 0.2):
        total = self.__calculer_total()
        return total * taux
    
 
    def afficher_commande(self):
        total = self.__calculer_total()
        print(f"Commande N°{self.__numéro}")
        print("Statut:", self.__statut)
        print("Plats commandés:")
        for nom, prix in self.__plats.items():
            print(f"- {nom}: {prix}€")
        print(f"Total à payer: {total}€")
        print(f"TVA (20%): {self.calculer_tva()}€")
    

commande1 = Commande(101)
commande1.ajouter_plat("Pizza montagnarde", 12.5)
commande1.ajouter_plat("Pâtes Carbonara", 14.0)
commande1.afficher_commande()
commande1.terminer_commande()
commande1.afficher_commande()