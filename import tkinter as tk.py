import tkinter as tk
import tkinter.messagebox
from tkinter.messagebox import YESNO
import random

def clear_board():
    global buttons, current_player, win

    buttons = []
    current_player = 'X'
    win = False

    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tk.Button(
                root, font=("Arial", 50), width=5, height=2, bg='darkgray',
                command=lambda r=row, c=column: place_symbol(r, c)
            )
            button.grid(row=row, column=column)
            button.config(text="")  # Clear button text
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)

def print_winner():
    global win

    if not win:
        win = True
        reponse = tk.messagebox.askquestion(title="Victoire !!!", message="Le joueur " + current_player + " a gagné, Voulez-vous faire une autre partie ?", icon='question', type=YESNO)
        if reponse == 'yes':
            clear_board()
            win = False  # Reset win flag
        else:
            root.quit()

def switch_player():
    global current_player
    current_player = '0' if current_player == 'X' else 'X'

def check_win(clicked_row, clicked_col):
    global win
    # Détecter victoire horizontale, verticale, diagonale
    if any([
        all(buttons[i][clicked_row]['text'] == current_player for i in range(3)),
        all(buttons[clicked_col][i]['text'] == current_player for i in range(3)),
        all(buttons[i][i]['text'] == current_player for i in range(3)),
        all(buttons[2 - i][i]['text'] == current_player for i in range(3))
    ]):
        print_winner()

    if not win:
        count = sum(buttons[col][row]['text'] in ['X', '0'] for col in range(3) for row in range(3))
        if count == 9:
            reponse = tk.messagebox.askquestion(title="Match Nul !!!", message="Il y a match nul, Voulez-vous faire une autre partie ?", icon='question', type=YESNO)
            if reponse == 'yes':
                clear_board()
            else:
                root.quit()

def place_symbol(row, column):
    global mode
    clicked_button = buttons[column][row]
    if clicked_button['text'] == "":
        clicked_button.config(text=current_player, fg='blue' if current_player == 'X' else 'red')
        check_win(row, column)
        switch_player()

        if mode.get() == 'IA' and current_player == '0' and not win:
            root.after(500, jouer_contre_ia)

def jouer_contre_ia():
    empty_buttons = [(r, c) for c in range(3) for r in range(3) if buttons[c][r]['text'] == ""]
    if empty_buttons:
        row, col = random.choice(empty_buttons)
        place_symbol(row, col)

def draw_grid():
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tk.Button(
                root, font=("Arial", 50), width=5, height=2, bg='darkgray',
                command=lambda r=row, c=column: place_symbol(r, c)
            )
            button.grid(row=row, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)

def choisir_mode():
    global mode
    mode = tk.StringVar()
    mode.set('Joueur')
    choix = tk.Toplevel(root)
    choix.title("Choisir le mode de jeu")
    tk.Label(choix, text="Choisissez le mode de jeu :").pack(pady=10)
    tk.Radiobutton(choix, text="Contre un autre joueur", variable=mode, value='Joueur').pack()
    tk.Radiobutton(choix, text="Contre l'IA", variable=mode, value='IA').pack()
    tk.Button(choix, text="Commencer", command=lambda: [choix.destroy(), clear_board()]).pack(pady=10)

# Stockages
buttons = []
current_player = 'X'
win = False

# Créer la fenêtre du jeu
root = tk.Tk()

# Personnalisation de la fenêtre
root.title("TicTacToe")
root.minsize(500, 500)

# Changer la couleur de fond de la fenêtre
root.configure(bg='darkgray')

choisir_mode()

root.mainloop()
