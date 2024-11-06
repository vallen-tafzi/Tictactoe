def afficher_plateau(plateau):
    for i in range(0, 9, 3):
        print(plateau[i] + " | " + plateau[i + 1] + " | " + plateau[i + 2])
        if i < 6:
            print("--+---+--")

def joueur_gagne(plateau, joueur):
    conditions_de_victoire = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for condition in conditions_de_victoire:
        if plateau[condition[0]] == plateau[condition[1]] == plateau[condition[2]] == joueur:
            return True
    return False

def case_vide(plateau):
    return " " in plateau

def mouvement_joueur(plateau, joueur):
    mouvement = int(input("Entrez un numéro de case (0-8): "))
    if plateau[mouvement] == " ":
        plateau[mouvement] = joueur
    else:
        print("Case déjà prise, essayez de nouveau.")
        mouvement_joueur(plateau, joueur)

def ia(plateau, signe):
    adversaire = "O" if signe == "X" else "X"
    for i in range(9):
        copie_plateau = plateau[:]
        if copie_plateau[i] == " ":
            copie_plateau[i] = signe
            if joueur_gagne(copie_plateau, signe):
                return i
    for i in range(9):
        copie_plateau = plateau[:]
        if copie_plateau[i] == " ":
            copie_plateau[i] = adversaire
            if joueur_gagne(copie_plateau, adversaire):
                return i
    coins = [0, 2, 6, 8]
    for coin in coins:
        if plateau[coin] == " ":
            return coin
    if plateau[4] == " ":
        return 4
    bords = [1, 3, 5, 7]
    for bord in bords:
        if plateau[bord] == " ":
            return bord
    return False

def jeu():
    plateau = [" " for _ in range(9)]
    print("Choisissez le mode de jeu :")
    print("1. Jouer contre un autre joueur")
    print("2. Jouer contre l'IA")
    choix = input("Entrez 1 ou 2 : ")
    
    joueur_actuel = "X"
    
    while case_vide(plateau) and not joueur_gagne(plateau, "X") and not joueur_gagne(plateau, "O"):
        afficher_plateau(plateau)
        if joueur_actuel == "X":
            mouvement_joueur(plateau, joueur_actuel)
            joueur_actuel = "O"
        else:
            if choix == "1":
                mouvement_joueur(plateau, joueur_actuel)
            elif choix == "2":
                mouvement = ia(plateau, joueur_actuel)
                if mouvement is not False:
                    plateau[mouvement] = joueur_actuel
            joueur_actuel = "X"
    
    afficher_plateau(plateau)
    if joueur_gagne(plateau, "X"):
        print("X gagne!")
    elif joueur_gagne(plateau, "O"):
        print("O gagne!")
    else:
        print("Match nul!")

jeu()
