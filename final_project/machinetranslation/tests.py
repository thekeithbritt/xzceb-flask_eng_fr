import unittest

from translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(), '') # test the null input of no text
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # test that 'Hello' in English is translated to French 'Bonjour'
        self.assertNotEqual(englishToFrench('Hello'), 'Hello') # test that 'Hello' in English is not translated to French


class TestF2E(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(frenchToEnglish(), '') # test the null input of no text
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test that 'Bonjour' in French is translated to English 'Hello'
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour') # test that 'Bonjour' in French is not translated to English

unittest.main()