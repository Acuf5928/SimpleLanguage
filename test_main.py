import unittest

from code_main import SimpleLanguage


class TestSimpleLanguage(unittest.TestCase):

    def test_init_with_out_value(self):
        # Create object to test
        toTest = SimpleLanguage()

        # Assert
        self.assertEqual(toTest.databasePath, "eng")
        self.assertEqual(toTest.actualLanguage, "eng")
        self.assertEqual(toTest.defaultLanguage, ".\\")
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
