class Part:
    """Représente une pièce du bateau."""
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        """Change le matériau de la pièce."""
        self.material = new_material

    def __str__(self):
        return f"{self.name} en {self.material}"


class Ship:
    """Représente un bateau avec ses pièces."""
    def __init__(self, name):
        self.name = name
        self.__parts = {
            "Mât": Part("Mât", "Bois"),
            "Coque": Part("Coque", "Bois"),
            "Gouvernail": Part("Gouvernail", "Fer")
        }
        self.history = []

    def display_state(self):
        """Affiche l'état actuel du bateau."""
        print(f"\nÉtat actuel du bateau {self.name}:")
        for part in self.__parts.values():
            print(f"  - {part}")

    def get_part(self, part_name):
        """Retourne une pièce si elle existe."""
        return self.__parts.get(part_name)

    def replace_part(self, part_name, new_part):
        """Remplace une pièce du bateau par une nouvelle."""
        if part_name in self.__parts:
            old_material = self.__parts[part_name].material
            self.__parts[part_name] = new_part  # Passage par référence
            self.history.append(f"Remplacement de {part_name} ({old_material}) par {new_part.material}")
            print(f"{part_name} a été remplacé par une pièce en {new_part.material}.")
        else:
            print(f"La pièce {part_name} n'existe pas.")

    def change_part(self, part_name, new_material):
        """Modifie directement le matériau d'une pièce existante."""
        part = self.get_part(part_name)
        if part:
            old_material = part.material
            part.change_material(new_material)  # Modification en mémoire
            self.history.append(f"Changement du matériau de {part_name} : {old_material} → {new_material}")
            print(f"{part_name} est maintenant en {new_material}.")
        else:
            print(f"La pièce {part_name} n'existe pas.")

    def display_history(self):
        """Affiche l'historique des modifications."""
        print("\nHistorique des modifications:")
        if self.history:
            for event in self.history:
                print(f"  - {event}")
        else:
            print("  - Aucune modification enregistrée.")


class RacingShip(Ship):
    """Un bateau de course avec une vitesse maximale."""
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        """Affiche la vitesse maximale du bateau de course."""
        print(f"Vitesse maximale du {self.name}: {self.max_speed} nœuds")


# Menu interactif
def main():
    ship = RacingShip("Thésée", 30)

    while True:
        print("\n=== Menu du Paradoxe de Thésée ===")
        print("1. Afficher l'état du bateau")
        print("2. Changer le matériau d'une pièce")
        print("3. Remplacer une pièce")
        print("4. Afficher l'historique des modifications")
        print("5. Afficher la vitesse du bateau")
        print("6. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            ship.display_state()
        elif choix == "2":
            part_name = input("Nom de la pièce (Mât, Coque, Gouvernail) : ")
            if ship.get_part(part_name):
                new_material = input(f"Entrez le nouveau matériau pour {part_name} : ")
                ship.change_part(part_name, new_material)
            else:
                print("Pièce invalide.")
        elif choix == "3":
            part_name = input("Nom de la pièce à remplacer (Mât, Coque, Gouvernail) : ")
            if ship.get_part(part_name):
                new_material = input(f"Matériau de la nouvelle pièce pour {part_name} : ")
                new_part = Part(part_name, new_material)
                ship.replace_part(part_name, new_part)
            else:
                print("Pièce invalide.")
        elif choix == "4":
            ship.display_history()
        elif choix == "5":
            ship.display_speed()
        elif choix == "6":
            print("Fin du programme.")
            break
        else:
            print("Option invalide, veuillez réessayer.")


# Exécution du programme
if __name__ == "__main__":
    main()
