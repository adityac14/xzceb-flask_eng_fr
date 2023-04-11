import unittest

from machinetranslation.translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        self.assertNotEqual(english_to_french(0), 0)
        
class TestF2E(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
        self.assertNotEqual(english_to_french(0), 0)


if __name__ == '__main__':
    unittest.main()