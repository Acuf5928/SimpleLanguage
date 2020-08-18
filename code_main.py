from code_exceptions import LanguageNotFoundException
from code_helper import LoadDatabaseList, foundDatabasesList


class SimpleLanguage:
    def __init__(self, defaultLanguage: str = "eng", actualLanguage: str = "eng", databasePath: str = ".\\language\\"):
        self.actualLanguage = actualLanguage
        self.databasePath = databasePath
        self.defaultLanguage = defaultLanguage

        self.strings = LoadDatabaseList(foundDatabasesList(self.databasePath))

    def changeLanguage(self, newLanguage: str):
        self.actualLanguage = newLanguage
        
    def changeDefaultLanguage(self, newDefaultLanguage: str):
        self.defaultLanguage = newDefaultLanguage

    def reloadDatabases(self):
        self.strings = LoadDatabaseList(foundDatabasesList(self.databasePath))
        # TODO: TEST, how?

    def rString(self, key: str, language: str = None) -> str:
        try:
            if language is not None:
                return self.strings[language][key]
            else:
                return self.strings[self.actualLanguage][key]

        except KeyError:
            try:
                return self.strings[self.defaultLanguage][key]
            except KeyError:
                raise LanguageNotFoundException("This language or this strings is not in our database")
