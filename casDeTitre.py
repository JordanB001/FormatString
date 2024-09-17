from Erreurs.verifications import pasUnStr, espaceNomPrenom

def casDeTitre(NomPrenom):
    """
    Verifie si la 1re lettre de chaque mot est en majuscule à partir d'une chaine de caractere
     et renvoie la chaine modifie avec la 1re lettre de chaque mot en majuscule, si c'est déjà le cas
     ne renvoie rien et affiche que la mise en forme est en cas de titre
    :param NomPrenom: Prends une chaine de caractere correspondant au Nom et au Prenoms
    :return: Renvoie un str
    """

    pasUnStr(NomPrenom)
    espaceNomPrenom(NomPrenom)

    nom = NomPrenom.split(" ")[0]
    prenom = NomPrenom.split(" ")[1]


    if (nom[0] == nom[0].upper()) and (prenom[0] == prenom[0].upper()):
        print("la mise en forme est deja en cas de titre")
    else:

        listeNom = []
        listePrenom = []

        for lettre in nom:
            listeNom.append(lettre)
        for lettre in prenom:
            listePrenom.append(lettre)

        listeNom[0] = listeNom[0].upper()
        listePrenom[0] = listePrenom[0].upper()

        nom = ""
        prenom = ""

        for i in range(len(listeNom)):
            nom = nom + str(listeNom[i])
        for i in range(len(listePrenom)):
            prenom = prenom + str(listePrenom[i])


        return nom + " " + prenom





