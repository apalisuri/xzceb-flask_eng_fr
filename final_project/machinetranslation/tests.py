from translator import englishtofrench,frenchtoenglish
import unittest

class testenfr(unittest.TestCase):
    def test_eng_fr(self):
        self.assertEqual(englishtofrench('Hello'),'Bonjour')
        self.assertEqual(englishtofrench('Rock'),'Rocher')
        self.assertEqual(englishtofrench('Sky'),'Ciel')
        self.assertEqual(englishtofrench(''),'Empty')

class testfren(unittest.TestCase):
    def test_fr_eng(self):
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')
        self.assertEqual(frenchtoenglish('Rocher'),'Rock')
        self.assertEqual(frenchtoenglish('Ciel'),'Sky')
        self.assertEqual(frenchtoenglish(''),'Empty')

unittest.main()