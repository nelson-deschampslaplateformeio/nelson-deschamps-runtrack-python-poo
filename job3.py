class Livre:
    def __init__(self, titre : str, auteur : str, nombre_de_pages : int):
        self.__titre = titre
        self.__auteur = auteur
        self.__disponible = True
        self.__nombre_de_pages = None
        self.set_nombre_de_pages(nombre_de_pages)

    # Accesseurs (Getters)
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages
        
    # Mutateurs (Setters)
    def set_titre(self, titre : str):
        self.__titre = titre

    def set_auteur(self, auteur : str):
        self.__auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages : int):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    
    # Vérification de la disponibilité
    def verification(self):
        return self.__disponible
    
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Livre emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible.")
        
   
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Livre rendu avec succès.")
        else:
            print("Le livre n'a pas été emprunté.")

    def afficher_détails_livre(self):
        print(f"titre : {self.__titre}, auteur : {self.__auteur}, nombre_de_pages : {self.__nombre_de_pages}, disponible : {self.__disponible}") 


livre1 = Livre("1984", "George Orwell", 328)
livre1.afficher_détails_livre()

livre1.emprunter()
livre1.afficher_détails_livre()

livre1.rendre()
livre1.afficher_détails_livre()
      

    

    