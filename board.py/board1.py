def afficher_plateau(plateau):
    for i in range(0, 9, 3):
        print(plateau[i] + " | " + plateau[i + 1] + " | " + plateau[i + 2])
        if i < 6:
            print("--+---+--")
