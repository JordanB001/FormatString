from Erreurs.verifications import pasUnStr

def anagramme(chaine1, chaine2):
    """
    Verifie si une paire chaine de caractere est un anagramme, renvoie True si c'est le cas
    :param chaine1: Chaine de caractere
    :param chaine2: Chaine de caractere
    :return: Renvoie un boolean
    """

    pasUnStr(chaine1)
    pasUnStr(chaine2)

    if len(chaine1) == len(chaine2):

        liste1 = []
        liste2 = []

        for lettre in chaine1:
            liste1.append(lettre)
        for lettre in chaine2:
            liste2.append(lettre)

        liste1.sort()
        liste2.sort()

        if liste1 == liste2:
            return True

    return False


