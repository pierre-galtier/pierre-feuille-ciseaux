import random

continuer = True

while continuer:

    choix_utilisateur = int(input("Pierre (0), Feuille (1) ou Ciseaux (2) ? : "))

    while choix_utilisateur != 0 and choix_utilisateur != 1 and choix_utilisateur != 2:
        choix_utilisateur = int(input("Pierre (0), Feuille (1) ou Ciseaux (2) ? : "))

    choix = ["Pierre", "Feuille", "Ciseaux"]
    print("Vous avez choisi " + choix[choix_utilisateur])

    choix_ordinateur = random.randint(0, 2)
    print("L'ordinateur a choisi " + str(choix[choix_ordinateur]))

    
    if choix_utilisateur == choix_ordinateur:
        print(" résultat : match nul")

    elif (choix_utilisateur == 0 and choix_ordinateur == 2) or (choix_utilisateur == 1 and choix_ordinateur == 0) or (choix_utilisateur == 2 and choix_ordinateur == 1): 
        print("résultat : vous avez gagné")
    else: 
        print("résultat : vous avez perdu")

    arreter = input("Souhaitez vous arrêter ? (o/n) ")
    if arreter == "o" or arreter == "O" :
        break