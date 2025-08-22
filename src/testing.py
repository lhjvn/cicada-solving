import unittest
from InstarCrypto import atbash, find_best_substitution, apply_shift
from LiberPrimus import get_section, runeToLatin
from PrimusFrequencies import normalized_freq_atbash
# Testing wether we can succesfully detect a substitution
class TestShiftDetection(unittest.TestCase):
    def setUp(self):
        self.ctx_s3 = atbash(get_section(4)) # Known solution @(ct) -> s3(ct) -> pt

    def test_substitution_detection(self):
        # Test the substitution detection
        self.keys3, _, _ = find_best_substitution(self.ctx_s3)
        self.assertTrue(self.keys3 == 3)

    def tearDown(self):
        print("[+] Finished testing shift detection")
        pass

class TestAtbashDetection(unittest.TestCase):
    def setUp(self):
        self.ctx_s3 = atbash(get_section(4))
        self.ctx_atbash = atbash(apply_shift(self.ctx_s3, 3))

    def test_atbash_detection(self):
        self.key, _, _ = find_best_substitution(self.ctx_atbash, list(range(29)), reference_freq=normalized_freq_atbash)
        self.assertTrue(self.key == 0) # key should be 0 since it matches the reference frequency

    def tearDown(self):
        print("[+] Finished testing atbash detection")
        pass

if __name__ == "__main__":
    unittest.main()
