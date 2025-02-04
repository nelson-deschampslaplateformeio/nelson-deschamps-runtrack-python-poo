class Voiture:
    def __init__(self, marque: str, modèle : str, année : int, kilométrage : int):
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__kilométrage = kilométrage
        self.__en_marche = False
        self.__réservoir = 50
    
    # Accesseurs (Getters)
    def get_marque(self):
        return self.__marque

    def get_modèle(self):
        return self.__modèle

    def get_année(self):
        return self.__année
    
    def get_kilométrage(self):
        return self.__kilométrage
    
    def get_en_marche(self):
        return self.__en_marche
    
    def get_réservoir(self):
        return self.__réservoir
        
    # Mutateurs (Setters)
    def set_marque(self, marque: str):
        self.__marque = marque

    def set_modèle(self, modèle : str):
        self.__modèle = modèle

    def set_année(self, année : int):
        self.__année = année

    def set_kilométrage(self, kilométrage : int) :
        self.__kilométrage = kilométrage
    
    def set_réservoir(self, réservoir, valeur: int):
        if valeur >= 0:
            self.__réservoir = valeur

    def _verification(self):
        return self.__en_marche
    
    def démarrer(self):
        if self._verification() > 5:
            self.__en_marche = True
            print("voiture démarrer avec succer")
        else:
            print("la voiture démarre")
    
    def arreter(self):
            self.__en_marche = False
            print("la voiture est à l'arret")

   
voiture1 = Voiture("Toyota", "Corolla", 2020, 30000)
voiture1.démarrer()
voiture1.arreter()
    

        