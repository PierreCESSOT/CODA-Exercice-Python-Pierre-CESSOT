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

def exercice21():
    print ("Exercice 21 : Test positif/négatif")
    nombre = float(input("Entrez un nombre : "))
    if nombre > 0:
        print(f"{nombre} est un nombre positif.")
    elif nombre < 0:
        print(f"{nombre} est un nombre négatif.")
    else:
        print("Vous avez entré zéro.")

def exercice22():
    print (" Exercice 22 : Majeur ou mineur")
    age = int(input("Entrez votre âge : "))
    if age >= 18:
        print("Vous êtes majeur.")
    else:
        print("Vous êtes mineur.")

def exercice23():
    print ("Exercice 23 : Note validée ou non")
    note = float(input("Entrez votre note (0-20) : "))
    if 0 <= note <= 20:
        if note >= 10:
            print("Note validée.")
        else:
            print("Note non validée.")
    else:
        print("Note invalide.")

def exercice24():
    print ("Exercice 24 : Le plus grand des deux nombres")
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    if nombre1 > nombre2:
        print(f"{nombre1} est le plus grand.")
    elif nombre2 > nombre1:
        print(f"{nombre2} est le plus grand.")
    else:
        print("Les deux nombres sont égaux.")

def exercice25():
    print ("Exercice 25 : ordre croissant ou decroissant")
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    if nombre1 < nombre2:
        print(f"{nombre1} < {nombre2}")
    elif nombre2 < nombre1:
        print(f"{nombre2} < {nombre1}")
    else:
        print("Les deux nombres sont égaux.")

def exercice26():
    print ("Exercice 26 : Divisible par 5")
    nombre = int(input("Entrez un nombre entier : "))
    if nombre % 5 == 0:
        print(f"{nombre} est divisible par 5.")
    else:
        print(f"{nombre} n'est pas divisible par 5.")

def exercice27():
    print ("Exercice 27 : Catégorie d'âge")
    age = int(input("Entrez votre âge : "))
    if 0 < age < 12:
        print("Vous êtes un enfant.")
    elif 12 <= age < 18:
        print("Vous êtes un adolescent.")
    elif age >= 18:
        print("Vous êtes un adulte.")
    else :
        print("Âge invalide.")

def exercice28():
    print ("Exercice 28 : Température de l'eau")
    temperature = float(input("Entrez la température de l'eau en °C : "))
    if temperature < 0:
        print("L'eau est à l'état solide.")
    elif 0 <= temperature < 100:
        print("L'eau est à l'état liquide.")
    elif temperature >= 100:
        print("L'eau est à l'état gazeux.")
    else:
        print("Température invalide.")

def exercice29():
    print ("Exercice 29 : Mention au bac")
    note = float(input("Entrez votre note au bac (0-20) : "))
    if 0 <= note < 10:
        print("Recalé")
    elif 10 <= note < 12:
        print("Mention : Passable")
    elif 12 <= note < 14:
        print("Mention : Assez bien")
    elif 14 <= note < 16:
        print("Mention : Bien")
    elif 16 <= note <= 20:
        print("Mention : Très bien")
    else:
        print("Note invalide.")

def exercice30():
    print ("Exercice 30 : Compter de 1 à N")
    n = int(input("Entrez un nombre entier N : "))
    for i in range(1, n + 1):
        print(i)

def exercice31():
    print ("Exercice 31 : Compte à rebours")
    n = int(input("Entrez un nombre entier N : "))
    for i in range(n, -1, -1):
        print(i)

def exercice32():
    print ("Exercice 32 : Somme jusqu'à N")
    n = int(input("Entrez un nombre entier N : "))
    somme = 0
    for i in range(1, n + 1):
         somme += i
    print(f"La somme des entiers de 1 à {n} est : {somme}")

def exercice33():
    print ("Exercice 33 : Table de multiplication")
    n = int(input("Entrez un nombre entier N : "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def exercice34():
    print ("Exercice 34 : Nombre pair jusqu'à N")
    n = int(input("Entrez un nombre entier N : "))
    for i in range(0, n + 1, 2):
        print(i)

def exercice35():
    print("Exercice 35 : carré parfait")
    n = int(input("Entrez un nombre entier N : "))
    for i in range(1, n + 1):
        if i * i <= n:
            print(f"{i} est un carré parfait.")
        else:
            print(f"{i} n'est pas un carré parfait.")

def exercice36():
    print("Exercice 36 : Répéter un mot")
    mot = input("Entrez un mot : ")
    n = int(input("Combien de fois voulez-vous le répéter ? "))
    for _ in range(n):
        print(mot)

def exercice37():
    print("Exercice 37 : Pyramide d'étoiles")
    n = int(input("Entrez le nombre de lignes pour la pyramide : "))
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

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
    elif choix == "21":
        exercice21()
    elif choix == "22":
        exercice22()
    elif choix == "23":
        exercice23()
    elif choix == "24":
        exercice24()
    elif choix == "25":
        exercice25()
    elif choix == "26":
        exercice26()
    elif choix == "27":
        exercice27()
    elif choix == "28":
        exercice28()
    elif choix == "29":
        exercice29()
    elif choix == "30":
        exercice30()
    elif choix == "31":
        exercice31()
    elif choix == "32":
        exercice32()
    elif choix == "33":
        exercice33()
    elif choix == "34":
        exercice34()
    elif choix == "35":
        exercice35()
    elif choix == "36":
        exercice36()
    elif choix == "37":
        exercice37()

    else: print("Exercice non reconnu.")
if __name__ == "__main__":
    main()