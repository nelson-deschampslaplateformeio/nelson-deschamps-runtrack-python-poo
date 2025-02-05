class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def afficher(self):
        print(f"Compte N°{self.__numero} - Titulaire: {self.__prenom} {self.__nom} - Solde: {self.__solde}€")
    
    def afficherSolde(self):
        print(f"Solde du compte {self.__numero}: {self.__solde}€")
    
    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant}€ effectué. Nouveau solde: {self.__solde}€")
    
    def retrait(self, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Fonds insuffisants pour effectuer ce retrait.")
        else:
            self.__solde -= montant
            print(f"Retrait de {montant}€ effectué. Nouveau solde: {self.__solde}€")
    
    def agios(self):
        if self.__solde < 0:
            frais = self.__solde * 0.05  # 5% d'agios sur le solde négatif
            self.__solde += frais
            print(f"Agios appliqués: {frais}€. Nouveau solde: {self.__solde}€")
    
    def virement(self, compte_destinataire, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Virement impossible, fonds insuffisants.")
        else:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant}€ vers le compte N°{compte_destinataire.__numero} effectué.")

# Création des comptes
compte1 = CompteBancaire(10000, "Dupont", "Jean", 1000)
compte2 = CompteBancaire(10001, "Martin", "Sophie", -200, decouvert=True)

# Affichage des comptes
compte1.afficher()
compte2.afficher()

# Opérations
compte1.versement(500)
compte1.retrait(200)
compte2.agios()
compte1.virement(compte2, 200)

# Affichage des comptes après opérations
compte1.afficherSolde()
compte2.afficherSolde()
