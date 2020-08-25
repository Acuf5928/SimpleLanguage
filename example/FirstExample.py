import SimpleLanguage


class FirstExampleClass:
    def __init__(self):
        # Init SimpleLanguage with default settings (defaultLanguage: eng, actualLanguage: eng, databasePath: ".\\language\\")
        lang = SimpleLanguage.init()

        # Take a text from database
        print(lang.rString("testKey1"))

        # But if we want a single text in a different language?
        print(lang.rString("testKey2", "ita"))

        # If we want to change actualLanguage?
        lang.changeLanguage("ita")
        print(lang.rString("testKey3"))

        # We have a possibility to change database path
        lang.changeDatabase(".\\language2")
        print(lang.rString("testKey4"))


if __name__ == "__main__":
    FirstExampleClass()
