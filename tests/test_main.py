import unittest

from SimpleLanguage.code_main import SimpleLanguage
from SimpleLanguage.code_exceptions import LanguageNotFoundException


class TestSimpleLanguage(unittest.TestCase):

    def test_init_with_out_value(self):
        # Create object to test
        toTest = SimpleLanguage()

        # Assert
        self.assertEqual(toTest.defaultLanguage, "eng")
        self.assertEqual(toTest.actualLanguage, "eng")
        self.assertEqual(toTest.databasePath, ".\\language\\")
        self.assertIsNotNone(toTest.strings)

    def test_init_with_databasePath(self):
        # Create object to test
        toTest = SimpleLanguage(databasePath="test")

        # Assert
        self.assertEqual(toTest.databasePath, "test")

    def test_init_with_actualLanguage(self):
        # Create object to test
        toTest = SimpleLanguage(actualLanguage="test")

        # Assert
        self.assertEqual(toTest.actualLanguage, "test")

    def test_init_with_defaultLanguage(self):
        # Create object to test
        toTest = SimpleLanguage(defaultLanguage="test")

        # Assert
        self.assertEqual(toTest.defaultLanguage, "test")

    def test_changeLanguage(self):
        # Create object to test
        toTest = SimpleLanguage(actualLanguage="old")

        # Manipulates
        toTest.changeLanguage("new")

        # Assert
        self.assertEqual(toTest.actualLanguage, "new")

    def test_changeDefaultLanguage(self):
        # Create object to test
        toTest = SimpleLanguage(defaultLanguage="old")

        # Manipulates
        toTest.changeDefaultLanguage("new")

        # Assert
        self.assertEqual(toTest.defaultLanguage, "new")

    def test_rString1(self):
        # Create object to test
        toTest = SimpleLanguage()

        # Manipulates
        toTest.strings = {"eng": {"string1": "result1eng"}, "ita": {"string1": "result1ita"}}

        # Assert
        self.assertEqual(toTest.rString("string1"), "result1eng")

    def test_rString2(self):
        # Create object to test
        toTest = SimpleLanguage()

        # Manipulates
        toTest.strings = {"eng": {"string1": "result1eng"}, "ita": {"string1": "result1ita"}}
        toTest.changeLanguage("ita")

        # Assert
        self.assertEqual(toTest.rString("string1"), "result1ita")

    def test_rString3(self):
        # Create object to test
        toTest = SimpleLanguage()

        # Manipulates
        toTest.strings = {"eng": {"string1": "result1eng"}}
        toTest.changeLanguage("ita")

        # Assert
        self.assertEqual(toTest.rString("string1"), "result1eng")

    def test_rString4(self):
        # Create object to test
        toTest = SimpleLanguage()

        # Manipulates
        toTest.strings = {"eng": {"string1": "result1eng"}, "ita": {"string1": "result1ita"}}

        # Assert
        self.assertRaises(LanguageNotFoundException, toTest.rString, "string2")

    def test_rString5(self):
        # Create object to test
        toTest = SimpleLanguage()

        # Manipulates
        toTest.strings = {"eng": {"string1": "result1eng"}, "ita": {"string1": "result1ita"}}
        toTest.changeDefaultLanguage("itas")
        toTest.changeLanguage("itas")

        # Assert
        self.assertRaises(LanguageNotFoundException, toTest.rString, "string1")

    def test_rString6(self):
        # Create object to test
        toTest = SimpleLanguage()

        # Manipulates
        toTest.strings = {"eng": {"string1": "result1eng"}, "ita": {"string1": "result1ita"}}

        # Assert
        self.assertEqual(toTest.rString("string1", "ita"), "result1ita")
