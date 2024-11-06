def afficher_plateau(plateau):
    print("\n")
    print(f" {plateau[0]} | {plateau[1]} | {plateau[2]} ")
    print("-----------")
    print(f" {plateau[3]} | {plateau[4]} | {plateau[5]} ")
    print("-----------")
    print(f" {plateau[6]} | {plateau[7]} | {plateau[8]} ")
    print("\n")

def verifier_victoire(plateau, joueur):
    # Lignes
    for i in range(0, 9, 3):
        if plateau[i] == plateau[i+1] == plateau[i+2] == joueur:
            return True
    # Colonnes
    for i in range(3):
        if plateau[i] == plateau[i+3] == plateau[i+6] == joueur:
            return True
    # Diagonales
    if plateau[0] == plateau[4] == plateau[8] == joueur:
        return True
    if plateau[2] == plateau[4] == plateau[6] == joueur:
        return True
    return False

def plateau_plein(plateau):
    return not any(isinstance(case, int) for case in plateau)

def coup_valide(plateau, coup):
    return isinstance(plateau[coup], int)

def tour_ia(plateau, ia_symbole):
    joueur_symbole = 'O' if ia_symbole == 'X' else 'X'
    
    # Vérifier si l'IA peut gagner au prochain coup
    for i in range(9):
        if coup_valide(plateau, i):
            plateau[i] = ia_symbole
            if verifier_victoire(plateau, ia_symbole):
                plateau[i] = i
                return i
            plateau[i] = i

    # Bloquer une victoire potentielle du joueur
    for i in range(9):
        if coup_valide(plateau, i):
            plateau[i] = joueur_symbole
            if verifier_victoire(plateau, joueur_symbole):
                plateau[i] = i
                return i
            plateau[i] = i

    # Prendre le centre s'il est libre
    if coup_valide(plateau, 4):
        return 4

    # Prendre les coins
    coins = [0, 2, 6, 8]
    coins_libres = [coin for coin in coins if coup_valide(plateau, coin)]
    if coins_libres:
        return coins_libres[0]

    # Prendre les côtés
    cotes = [1, 3, 5, 7]
    cotes_libres = [cote for cote in cotes if coup_valide(plateau, cote)]
    if cotes_libres:
        return cotes_libres[0]

def main():
    while True:
        plateau = list(range(9))
        print("\nBienvenue au jeu du Morpion!")
        mode = input("Choisissez le mode de jeu:\n1. Joueur contre Joueur\n2. Joueur contre IA\nVotre choix (1 ou 2): ")
        
        if mode not in ['1', '2']:
            print("Choix invalide. Veuillez choisir 1 ou 2.")
            continue
            
        joueur_actuel = 'X'
        
        while True:
            afficher_plateau(plateau)
            
            if mode == '2' and joueur_actuel == 'O':
                print("Tour de l'IA...")
                coup = tour_ia(plateau, 'O')
            else:
                print(f"Tour du Joueur {joueur_actuel}")
                try:
                    coup = int(input(f"Entrez un nombre entre 0 et 8: "))
                    if coup < 0 or coup > 8:
                        print("Nombre invalide! Choisissez entre 0 et 8.")
                        continue
                except ValueError:
                    print("Entrée invalide! Veuillez entrer un nombre.")
                    continue
                
            if not coup_valide(plateau, coup):
                print("Case déjà occupée!")
                continue
                
            plateau[coup] = joueur_actuel
            
            if verifier_victoire(plateau, joueur_actuel):
                afficher_plateau(plateau)
                if mode == '2' and joueur_actuel == 'O':
                    print("L'IA a gagné!")
                else:
                    print(f"Le Joueur {joueur_actuel} a gagné!")
                break
                
            if plateau_plein(plateau):
                afficher_plateau(plateau)
                print("Match nul!")
                break
                
            joueur_actuel = 'O' if joueur_actuel == 'X' else 'X'
            
        if input("\nVoulez-vous rejouer? (o/n): ").lower() != 'o':
            break
            
    print("Merci d'avoir joué!")

if __name__ == "__main__":
    main()
