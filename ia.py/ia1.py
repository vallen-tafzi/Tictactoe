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
