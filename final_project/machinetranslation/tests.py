import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french('null'), 'Bonjour') # test the null input to ensure no translation to French
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test that 'Hello' in English is translated to French 'Bonjour'


class TestF2E(unittest.TestCase): 
    def test2(self): 
        self.assertNotEqual(french_to_english('null'), 'Hello') # test the null input to ensure no translation to English
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test that 'Bonjour' in French is translated to English 'Hello'

unittest.main()