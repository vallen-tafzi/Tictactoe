import random


def __init__(self) :
        self.board = []
        
def create_board(self) :
        for i in range(3) :
            row = []
            for j in range(3) :
                row.append('-')
            self.board.append(row)

def get_random_first_player(self) :
        return random.randint(0, 1)

def fix_spot(self, row, col, player) :
        self.board[row][col] = joueur

def is_player_win(self, player) :
        win = None

        n = len(self.board)

        # vérification des lignes
        for i in range(n) :
            win = True
            for j in range(n) :
                si self.board[i][j]!= joueur :
                    victoire = Faux
                    break
            si victoire :
                return win

        # vérification des colonnes
        for i in range(n) :
            win = True
            for j in range(n) :
                si self.board[j][i]!= joueur :
                    victoire = Faux
                    break
            si victoire :
                return win

        # vérification des diagonales
        win = True
        pour i dans range(n) :
            si self.board[i][i]!= player :
                win = False
                break
        si victoire :
            return win

        win = True
        for i in range(n) :
            si self.board[i][n - 1 - i] != player :
                victoire = Faux
                break
        si victoire :
            return win
        retour Faux

        for row in self.board :
            for item in row :
                si élément == '-' :
                    return False
        return True

    def is_board_filled(self) :
        for row in self.board :
            for item in row :
                if item == '-' :
                    return False
        return True

    def swap_player_turn(self, player) :
        return 'X' if player == 'O' else 'O'

    def show_board(self) :
        for row in self.board :
            for item in row :
                print(item, end=" ")
            print()

    def start(self) :
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True :
            print(f "Tour du joueur {joueur}")

            self.show_board()

            # prise en compte des données de l'utilisateur
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot : ").split()))
            print()

            # fixation de la tache
            self.fix_spot(row - 1, col - 1, player)

            # vérifier si le joueur actuel a gagné ou non
            if self.is_player_win(player) :
                print(f "Le joueur {joueur} gagne la partie !")
                break

            # vérifier si la partie est nulle ou non
            if self.is_board_filled() :
                print("Match nul !")
                break

            # échanger le tour
            joueur = self.swap_player_turn(joueur)

        # afficher la vue finale du plateau
        print()
        self.show_board()


# démarrer le jeu
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
