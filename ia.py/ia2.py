def ia(plateau, signe):
    # L'IA identifie d'abord qui est l'adversaire
    adversaire = "O" if signe == "X" else "X"
    
    # PRIORITÉ 1 : Gagner si possible
    for i in range(9):
        copie_plateau = plateau[:]  # Fait une copie du plateau
        if copie_plateau[i] == " ":  # Si la case est vide
            copie_plateau[i] = signe  # Teste le coup
            if joueur_gagne(copie_plateau, signe):  # Vérifie si ce coup permet de gagner
                return i  # Si oui, joue ce coup
    
    # PRIORITÉ 2 : Bloquer l'adversaire s'il peut gagner
    for i in range(9):
        copie_plateau = plateau[:]
        if copie_plateau[i] == " ":
            copie_plateau[i] = adversaire  # Simule le coup de l'adversaire
            if joueur_gagne(copie_plateau, adversaire):  # Si l'adversaire peut gagner
                return i  # Bloque cette case
    
    # PRIORITÉ 3 : Prendre les coins libres
    coins = [0, 2, 6, 8]  # Positions des coins
    for coin in coins:
        if plateau[coin] == " ":
            return coin
    
    # PRIORITÉ 4 : Prendre le centre
    if plateau[4] == " ":
        return 4
    
    # PRIORITÉ 5 : Prendre les bords
    bords = [1, 3, 5, 7]
    for bord in bords:
        if plateau[bord] == " ":
            return bord