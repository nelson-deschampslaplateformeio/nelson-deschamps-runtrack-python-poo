class Student:
    def __init__(self, nom: str, prénom: str, numéro_étudiant: int):
        self.__nom = nom
        self.__prénom = prénom
        self.__numéro_étudiant = numéro_étudiant
        self.__nombre_de_crédits = 0
        self.__level = self.__student_eval()
       
    # Accesseurs (Getters)
    def get_nom(self):
        return self.__nom

    def get_prénom(self):
        return self.__prénom
    
    def get_numéro_étudiant(self):
        return self.__numéro_étudiant
    
    def get_nombre_de_crédits(self):
        return self.__nombre_de_crédits
    
    # Ajouter des crédits
    def add_nombre_de_crédits(self, nombre: int):
        if isinstance(nombre, int) and nombre > 0:
            self.__nombre_de_crédits += nombre
            self.__level = self.__student_eval()
        else:
            print("Erreur : Le nombre de crédits doit être un entier positif.")

    # Méthode privée pour évaluer le niveau de l'étudiant
    def __student_eval(self):
        if self.__nombre_de_crédits >= 90:
            return "Excellent"
        elif self.__nombre_de_crédits >= 80:
            return "Très bien"
        elif self.__nombre_de_crédits >= 70:
            return "Bien"
        elif self.__nombre_de_crédits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def afficher_étudiant(self):
        print(f"Le nombre de credits de {self.__prénom} {self.__nom} est de {self.__nombre_de_crédits} points")
    
    def student_info(self):
        print(f"Nom = {self.__prénom}\nPrénom = {self.__nom}\nid = {self.__numéro_étudiant}\nNiveau = {self.__level}")
    

etudiant1 = Student("Doe", "John", 145)
etudiant1.add_nombre_de_crédits(30)
etudiant1.add_nombre_de_crédits(30)
etudiant1.add_nombre_de_crédits(10)
etudiant1.afficher_étudiant()
etudiant1.student_info()
