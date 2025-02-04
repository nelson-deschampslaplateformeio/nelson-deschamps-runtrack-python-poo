class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("Résultat de l'addition :", resultat)


nombre1 = int(input("Entrez la valeur de nombre1 : "))
nombre2 = int(input("Entrez la valeur de nombre2 : "))

# Instanciation de la classe avec les valeurs choisies
operation_instance = Operation(nombre1, nombre2)

print(operation_instance)

print("nombre1:", operation_instance.nombre1)
print("nombre2:", operation_instance.nombre2)

# Appel de la méthode addition
operation_instance.addition()