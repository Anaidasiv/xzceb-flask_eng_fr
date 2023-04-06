import unittest
from translator import french_to_english,english_to_french

class TestEnglish(unittest.TestCase):
   def test1(self):
       # Test translation of "Hello" from English to French
       result = french_to_english("Bonjour")
       assert result == "Hello"
       result = french_to_english("Nom")
       assert result == "Name"

class TestFrench(unittest.TestCase):
   def test1(self):
       # Test translation of "Hello" from English to French
       result = english_to_french("Hello")
       assert result == "Bonjour"
       result = english_to_french("Name")
       assert result == "Nom"

unittest.main()           


