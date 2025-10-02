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
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()