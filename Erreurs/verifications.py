from Erreurs.exceptions import PasUnStr, NomPrenom

def pasUnStr(variable):
    if type(variable) != str:
        raise PasUnStr

def espaceNomPrenom(variable):
    if not (" " in variable):
        raise NomPrenom



