import unittest
from habitant import Habitant
from personnes import Adulte, Enfant

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
            
            
if __name__ == "__main__":
    unittest.main(verbosity=2)