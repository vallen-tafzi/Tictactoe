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
