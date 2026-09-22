import unittest
from habitant import Habitant
from personnes import Adulte, Enfant
from village import Village

class TestHabitant(unittest.TestCase):
    """Tests pour la classe Habitant et l’encapsulation."""
    def setUp(self):
        self.habitant = Adulte("Dupont", "Marie", 35, "Rue A", {"vaches": 3})
        
    def test_compte_animal_cas_limite(self):
        self.assertEqual(self.habitant.compte_animal("moutons"), 0)

    def test_age_setter_valide(self): 
        self.habitant.age = 26
        self.assertEqual(self.habitant.age, 26)

    def test_age_setter_invalide(self):
        with self.assertRaises(ValueError):
            self.habitant.age = -7

class TestVillage(unittest.TestCase):
    """Tests pour la classe Village : composition et agregation."""

    def setUp(self):
        self.village = Village("PyTown")

    def test_ajouter_habitant_composition(self):
        """Cas usuel : le village cree et possede un nouvel habitant."""
        self.village.ajouter_habitant_composition("Aldric", "Aldric", 25, "Rue A", {"vaches": 3})
        self.assertEqual(len(self.village.get_habitants()), 1)

    def test_ajouter_habitant_agregation_deux_villages(self):
        """Cas limite : un meme habitant ajoute par agregation a deux villages."""
        melia= Adulte("Melia", "Melia", 28, "Rue B", {"poules": 10})
        autre_village = Village("VillageVoisin")

        self.village.ajouter_habitant_agregation(melia)
        autre_village.ajouter_habitant_agregation(melia)

        self.assertIn(melia, self.village.get_habitants())
        self.assertIn(melia, autre_village.get_habitants())  
                  
class TestHeritage(unittest.TestCase):
    """Tests pour l'heritage : calcul_nombre_annee_avant_retraite."""

    def test_calcul_retraite_adulte(self):
        adulte = Adulte("Dupont", "Marie", 35, "Rue A")
        self.assertEqual(adulte.calcul_nombre_annee_avant_retraite(), 27)

    def test_calcul_retraite_enfant(self):
        enfant = Enfant("Martin", "Lucas", 12, "Rue B")
        self.assertIn("enfant", enfant.calcul_nombre_annee_avant_retraite())

    def test_enfant_age_invalide(self):
        with self.assertRaises(ValueError):
            Enfant("Oups", "X", 20, "Rue C")
                       
if __name__ == "__main__":
    unittest.main(verbosity=2)