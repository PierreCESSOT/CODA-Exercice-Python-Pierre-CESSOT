def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    print("Exercice 2 : Afficher son prenom")
    prenom = input("Entrez votre prénom : ")
    print(f"Bonjour, {prenom} !")

def exercice3():
    print("Exercice 3 : Afficher trois lignes")
    print("Première ligne\nDeuxième ligne\nTroisième ligne")

def exercice4():
    print ("Exercice 4 : Calculer l'âge")
    annee_naissance = int(input("Entrez votre année de naissance : "))
    age = 2025 - annee_naissance
    print(f"Vous avez {age} ans.")

def exercice5():
    print ("Exercice 5 : Addition simple")
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    somme = nombre1 + nombre2
    print(f"La somme des deux nombres est : {somme}")

def exercice6():
    print ("Exercice 6 : Soustraction simple")
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    resultat = nombre1 - nombre2
    print(f"Le résultat de la soustraction est : {resultat}")

def exercice7():
    print ("Exercice 7 : Multiplication simple")
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    produit = nombre1 * nombre2
    print(f"Le produit des deux nombres est : {produit}")

def exercice8():
    print ("Exercice 8 : Division simple")
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    quotient = nombre1 / nombre2
    print(f"Le quotient des deux nombres est : {quotient}")

def exercice9():
    print ("Exercice 9 : Carré d'un nombre")
    nombre = float(input("Entrez un nombre : "))
    carre = nombre ** 2
    print(f"Le carré de {nombre} est : {carre}")

def exercice10():
    print ("Exercice 10 : Double d'un nombre")
    nombre = float(input("Entrez un nombre : "))
    double = nombre * 2
    print(f"Le double de {nombre} est : {double}")

def exercice11():
    print ("Exercice 11 : Moitié d'un nombre")
    nombre = float(input("Entrez un nombre : "))
    moitie = nombre / 2
    print(f"La moitié de {nombre} est : {moitie}")

def exercice12():
    print ("Exercice 12 : Afficher 5 fois")
    for i in range(5):
        print("Bonjour")

def exercice13():
    print ("Exercice 13 : Compter jusqu'à 5")
    for i in range(1, 6):
        print(i)

def exercice14():
    print ("Exercice 14 : Table de 2")
    for i in range(1, 11):
        print(f"2 x {i} = {2 * i}")

def exercice15():
    print ("Exercice 15 : périmètre d'un carré")
    cote = float(input("Entrez la longueur du côté du carré : "))
    perimetre = 4 * cote
    print(f"Le périmètre du carré est : {perimetre}")

def exercice16():
    print ("Exercice 16 : Aire d'un carré")
    cote = float(input("Entrez la longueur du côté du carré : "))
    aire = cote ** 2
    print(f"L'aire du carré est : {aire}")

def exercice17():
    print ("Exercice 17 : convertion euros en dollars")
    euros = float(input("Entrez le montant en euros : "))
    dollars = euros * 1.1
    print(f"{euros} euros est égal à {dollars} dollars.")

def exercice18():
    print ("Exercice 18 : Convertion minutes en secondes")
    minutes = float(input("Entrez le nombre de minutes : "))
    secondes = minutes * 60
    print(f"{minutes} minutes est égal à {secondes} secondes.")

def exercice19():
    print ("Exercice 19 : Prix TTC")
    prix_ht = float(input("Entrez le prix HT : "))
    tva = 0.2
    prix_ttc = prix_ht * (1 + tva)
    print(f"Le prix TTC est : {prix_ttc}")

def exercice20():
    print ("Exercice 20 : Message personnalisé")
    nom = input("Entrez votre nom : ")
    age = input("Entrez votre âge : ")
    print(f"Bonjour {nom}, vous avez {age} ans.")

def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    elif choix == "4":
        exercice4()
    elif choix == "5":
        exercice5()
    elif choix == "6":
        exercice6()
    elif choix == "7":
        exercice7()
    elif choix == "8":
        exercice8()
    elif choix == "9":
        exercice9()
    elif choix == "10":
        exercice10()
    elif choix == "11":
        exercice11()
    elif choix == "12":
        exercice12()
    elif choix == "13":
        exercice13()
    elif choix == "14":
        exercice14()
    elif choix == "15":
        exercice15()
    elif choix == "16":
        exercice16()
    elif choix == "17":
        exercice17()
    elif choix == "18":
        exercice18()
    elif choix == "19":
        exercice19()
    elif choix == "20":
        exercice20()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()