from Erreurs.verifications import pasUnStr

def enleverAccents(chaine):
    """
    Permets d'enlever les accents d'une chaine de caractere et la renvoie sans
    :param chaine: Prends une chaine de caractere sans majuscules
    :return: Renvoie une chaine de caractere sans les accents
    """

    pasUnStr(chaine)

    chaineSansAccent = chaine
    listeAccentsA = ["à", "â"]
    listeAccentsE = ["é", "è", "ê"]
    listeAccentsI = ["î"]
    listeAccentsO = ["ô"]
    listeAccentsU = ["ù", "û"]


    for accent in listeAccentsA:
        chaineSansAccent = chaineSansAccent.replace(accent, "a")
    for accent in listeAccentsE:
        chaineSansAccent = chaineSansAccent.replace(accent, "e")
    for accent in listeAccentsI:
        chaineSansAccent = chaineSansAccent.replace(accent, "i")
    for accent in listeAccentsO:
        chaineSansAccent = chaineSansAccent.replace(accent, "o")
    for accent in listeAccentsU:
        chaineSansAccent = chaineSansAccent.replace(accent, "u")

    return chaineSansAccent
