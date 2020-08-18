from SimpleLanguage.code_main import SimpleLanguage


def init(defaultLanguage: str = "eng", actualLanguage: str = "eng", databasePath: str = ".\\language\\"):
    return SimpleLanguage(defaultLanguage, actualLanguage, databasePath)