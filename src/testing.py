import unittest
from InstarCrypto import atbash, find_best_substitution
from LiberPrimus import get_section, runeToLatin

# Testing wether we can succesfully detect a substitution
class TestSubstitutionDetection(unittest.TestCase):
    def setUp(self):
        # Code that runs before each test
        self.ciphertext = atbash(get_section(4))

    def test_substitution_detection(self):
        # Test the substitution detection
        self.key, _, _ = find_best_substitution(self.ciphertext)
        self.assertTrue(self.key == 3)

    def tearDown(self):
        # Code that runs after each test
        pass


if __name__ == "__main__":
    unittest.main()
