import unittest
from InstarCrypto import atbash, findBestSubstitution, applyShift
from LiberPrimus import getSection
from PrimusFrequencies import NORMALIZED_FREQ_ATBASH
# Testing wether we can succesfully detect a substitution
class TestShiftDetection(unittest.TestCase):
    def setUp(self):
        self.ctx_s3 = atbash(getSection(4)) # Known solution @(ct) -> s3(ct) -> pt

    def test_substitution_detection(self):
        # Test the substitution detection
        self.keys3, _, _ = findBestSubstitution(self.ctx_s3)
        self.assertTrue(self.keys3 == 3)

    def tearDown(self):
        print("\n[+] Finished testing shift detection")
        pass

class TestAtbashDetection(unittest.TestCase):
    def setUp(self):
        self.ctx_s3 = atbash(getSection(4))
        self.ctx_atbash = atbash(applyShift(self.ctx_s3, 3))

    def test_atbash_detection(self):
        self.key, _, _ = findBestSubstitution(self.ctx_atbash, reference_freq=NORMALIZED_FREQ_ATBASH)
        self.assertTrue(self.key == 0) # key should be 0 since it matches the reference frequency
        print()

    def tearDown(self):
        print("\n[+] Finished testing atbash detection")
        pass

if __name__ == "__main__":
    unittest.main()
