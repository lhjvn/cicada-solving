import unittest
from InstarCrypto import atbash, findBestSubstitution, applyShift, applyMultiShift
from LiberPrimus import getSection
from PrimusFrequencies import NORMALIZED_FREQ_ATBASH


class TestShiftEncryption(unittest.TestCase):

    def setUp(self):
        pass

    def testSingleShift(self):
        self.assertEqual(applyShift("ᚠ", 3), "ᚩ") # ᚠ = 0 =3> ᚩ=3
        self.assertEqual(applyShift("ᚠ", -3), "ᚣ") # ᚠ = 0 =-3> 26
        self.assertEqual(applyShift("lorem ipsum", 4), "lorem ipsum") # we only allow operations on runes

        print("\n[+] Finished testing single shift")

    def testMultiShift(self):
        self.assertEqual(applyMultiShift("ᚠ", [3, -3]), "ᚩ") # ᚠ = 0 =3> ᚩ=3 =-3> ᚣ=26
        self.assertEqual(applyMultiShift("ᚠabcᚠ", [3, -3]), "ᚩabcᚣ") # ᚠ = 0 =3> ᚩ=3 =1> ᚪ=4
        self.assertEqual(applyMultiShift("lorem ipsum", [4]), "lorem ipsum") # we only allow operations on runes
        print("\n[+] Finished testing multi shift")


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
