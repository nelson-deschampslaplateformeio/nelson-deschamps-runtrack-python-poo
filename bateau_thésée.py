import tkinter as tk
from tkinter import simpledialog, messagebox
import random

# Classe Part représentant une pièce du bateau
class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        self.material = new_material

    def __str__(self):
        return f"{self.name} en {self.material}"

# Classe Ship représentant un bateau
class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {
            "Mât": Part("Mât", "Bois"),
            "Coque": Part("Coque", "Bois"),
            "Gouvernail": Part("Gouvernail", "Fer")
        }
        self.history = []

    def display_state(self):
        state = f"État actuel du bateau {self.name}:\n"
        for part in self.__parts.values():
            state += f"  - {part}\n"
        return state

    def get_part(self, part_name):
        return self.__parts.get(part_name)

    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            old_material = self.__parts[part_name].material
            self.__parts[part_name] = new_part
            self.history.append(f"Remplacement de {part_name} ({old_material}) par {new_part.material}")
        else:
            print(f"La pièce {part_name} n'existe pas.")

    def change_part(self, part_name, new_material):
        part = self.get_part(part_name)
        if part:
            old_material = part.material
            part.change_material(new_material)
            self.history.append(f"Changement du matériau de {part_name} : {old_material} → {new_material}")
        else:
            print(f"La pièce {part_name} n'existe pas.")

    def display_history(self):
        return "\n".join(self.history) if self.history else "Aucune modification enregistrée."

# Interface utilisateur avec Tkinter
class ShipApp:
    def __init__(self, root, ship):
        self.ship = ship
        self.root = root
        self.root.title("Bateau de Thésée")

        self.label = tk.Label(root, text=self.ship.display_state(), justify="left")
        self.label.pack(pady=10)

        self.change_btn = tk.Button(root, text="Changer un matériau", command=self.change_material)
        self.change_btn.pack()

        self.replace_btn = tk.Button(root, text="Remplacer une pièce", command=self.replace_part)
        self.replace_btn.pack()

        self.history_btn = tk.Button(root, text="Afficher l'historique", command=self.show_history)
        self.history_btn.pack()

        self.event_btn = tk.Button(root, text="Événement aléatoire", command=self.random_event)
        self.event_btn.pack()

    def refresh_display(self):
        self.label.config(text=self.ship.display_state())

    def change_material(self):
        part_name = simpledialog.askstring("Changer matériau", "Nom de la pièce (Mât, Coque, Gouvernail) :")
        if part_name in self.ship.get_part(part_name):
            new_material = simpledialog.askstring("Nouveau matériau", f"Matériau pour {part_name} :")
            if new_material:
                self.ship.change_part(part_name, new_material)
                self.refresh_display()
        else:
            messagebox.showerror("Erreur", "Pièce invalide.")

    def replace_part(self):
        part_name = simpledialog.askstring("Remplacement", "Nom de la pièce (Mât, Coque, Gouvernail) :")
        if part_name in self.ship.get_part(part_name):
            new_material = simpledialog.askstring("Matériau", f"Matériau de la nouvelle pièce pour {part_name} :")
            if new_material:
                new_part = Part(part_name, new_material)
                self.ship.replace_part(part_name, new_part)
                self.refresh_display()
        else:
            messagebox.showerror("Erreur", "Pièce invalide.")

    def show_history(self):
        messagebox.showinfo("Historique", self.ship.display_history())

    def random_event(self):
        events = [
            ("Le mât a été endommagé par une tempête!", "Mât", "Acier"),
            ("La coque a pris l'eau, elle doit être renforcée!", "Coque", "Carbone"),
            ("Le gouvernail est rouillé!", "Gouvernail", "Inox")
        ]
        event = random.choice(events)
        messagebox.showinfo("Événement", event[0])
        self.ship.change_part(event[1], event[2])
        self.refresh_display()

# Exécution du programme
if __name__ == "__main__":
    my_ship = Ship("Thésée")
    root = tk.Tk()
    app = ShipApp(root, my_ship)
    root.mainloop()
