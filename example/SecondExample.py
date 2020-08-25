import SimpleLanguage
from SimpleLanguage.code_exceptions import LanguageNotFoundException, DatabaseNotFoundException


class SecondExampleClass:
    def __init__(self):
        # Init SimpleLanguage with our settings
        lang = SimpleLanguage.init(defaultLanguage="eng", actualLanguage="ita", databasePath=".\\language2")

        # Take a text from database
        print(lang.rString("testKey5"))

        # But if we search a key that doesnt exist in actualLanguage language? take a string from defaultLanguage:
        print(lang.rString("testKey6"))

        # If we search a key that doesnt exist in at all? Raise LanguageNotFoundException
        try:
            print(lang.rString("testKey7"))
        except LanguageNotFoundException as Ex:
            print(Ex)

        # If we set a database path that doesnt exist? Raise DatabaseNotFoundException
        try:
            lang.changeDatabase(".\\not\\exist\\database")
        except DatabaseNotFoundException as Ex:
            print(Ex)


if __name__ == "__main__":
    SecondExampleClass()
