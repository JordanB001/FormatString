from Formatage.accents import enleverAccents
from Erreurs.verifications import pasUnStr

def palindrome(chaine):
    """
    Verifie si la chaine(str) est un palindrome, renvoie True si c'est un palindrome
    :param chaine: Prends une chaine de caractere
    :return: Renvoie un boolean
    """

    pasUnStr(chaine)

    chaineSansEspace = chaine.replace(' ', '')
    chaineSansEspace = chaineSansEspace.lower()
    chaineALEnver = ""


    lettreListe = []
    for lettre in chaineSansEspace:
        lettreListe.append(lettre)

    chaineSansEspaceEtAccent = enleverAccents(chaineSansEspace)

    for i in range(len(lettreListe)):
        chaineALEnver = str(chaineALEnver + chaineSansEspaceEtAccent[- (1 + i)])

    if str(chaineSansEspaceEtAccent) == str(chaineALEnver):
        return True


    return False










