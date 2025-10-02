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
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()