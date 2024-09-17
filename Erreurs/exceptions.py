

class MyAppException(Exception):
    pass

class PasUnStr(MyAppException):
    def __init__(self, message="La variable n'est pas une chaine de caractere !", *args, **kwargs):
        super().__init__(message, *args, **kwargs)

class NomPrenom(MyAppException):
    def __init__(self, message="Il faut un nom et un prenom espacé d'un espace !", *args, **kwargs):
        super().__init__(message, *args, **kwargs)

