from habitant import Habitant

class Village() :
    # un constructeur qui permet d'instancier un objet de classe Village
    def __init__(self , nom) : 
        self.nom = nom
        self.habitants =[]
    
    # Accesseurs
    def get_habitants(self):
        return self.habitants 
          
    # Methode pour ajouter un habitant a la liste 
    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None):
        """Cree un nouvel Habitant et l'ajoute au village ."""
        habitant = Adulte(nom, prenom, age, adresse, animaux)
        self.habitants.append(habitant)
        
    def ajouter_habitant_agregation(self, habitant) :
        """Ajoute un Habitant deja existant au village."""
        self.habitants.append(habitant)
    
    #Methode qui affiche chaque habitant du village
    def afficher_habitants(self) :
        for habitant in self.habitants :
            print( f"{habitant}")
            
if __name__ == "__main__":
    pytown = Village("PyTown")
    pytown.ajouter_habitant_composition("Aldric", "Aldric", 25, "Rue A", {"vaches": 3})
    elise = Adulte("Elise", "Elise", 28, "Rue B", {"poules": 10})
    pytown.ajouter_habitant_agregation(elise)

    autre_village = Village("VillageVoisin")
    autre_village.ajouter_habitant_agregation(elise)

    assert len(pytown.get_habitants()) == 2
    assert elise in autre_village.get_habitants()
    print("Tests village OK")

# ajouter_habitant_composition illustre une relation de composition car le Village
# cree lui-meme l'objet Habitant : ce dernier n'existe pas avant l'appel et n'a
# de sens que rattache a ce village precis .
# ajouter_habitant_agregation illustre au contraire une agregation : le Village
# recoit un objet Habitant qui existe deja independamment de lui, et peut donc
# appartenir a plusieurs villages en meme temps.