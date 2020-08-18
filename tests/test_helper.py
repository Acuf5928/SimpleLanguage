import unittest

from SimpleLanguage.code_exceptions import DatabaseNotFoundException
from SimpleLanguage.code_helper import foundDatabasesList, LoadDatabaseList


class TestSimpleLanguage(unittest.TestCase):

    def test_foundDatabasesList1(self):
        # Create object to test
        pathList = foundDatabasesList(".\\test_db1")

        # Expected
        expected = ['.\\test_db1\\eng.json', '.\\test_db1\\ita.json']

        # Assert
        self.assertEqual(pathList, expected)

    def test_foundDatabasesList2(self):
        # Create object to test
        pathList = foundDatabasesList(".\\test_db1/")

        # Expected
        expected = ['.\\test_db1\\eng.json', '.\\test_db1\\ita.json']

        # Assert
        self.assertEqual(pathList, expected)

    def test_foundDatabasesList3(self):
        # Create object to test
        pathList = foundDatabasesList(".\\test_db1\\")

        # Expected
        expected = ['.\\test_db1\\eng.json', '.\\test_db1\\ita.json']

        # Assert
        self.assertEqual(pathList, expected)

    def test_foundDatabasesList4(self):
        # Create object to test
        pathList = foundDatabasesList(".\\test_db2\\")

        # Manipulates
        #toTest.changeLanguage("new")

        # Expected
        expected = []

        # Assert
        self.assertEqual(pathList, expected)

    def test_LoadDatabaseList1(self):
        # Create object to test
        pathList = LoadDatabaseList([])

        # Expected
        expected = {}

        # Assert
        self.assertEqual(pathList, expected)

    def test_LoadDatabaseList2(self):
        # Create object to test
        pathList = LoadDatabaseList(['.\\test_db1\\eng.json', '.\\test_db1\\ita.json'])

        # Expected
        expected = {'eng': {'testKey': 'testResultEng'}, 'ita': {'testKey': 'testResultIta'}}

        # Assert
        self.assertEqual(pathList, expected)

    def test_LoadDatabaseList3(self):
        # Create object to test and assert
        self.assertRaises(DatabaseNotFoundException, LoadDatabaseList, (['\\path\\to\\not\\Exists\\Files.json']))
