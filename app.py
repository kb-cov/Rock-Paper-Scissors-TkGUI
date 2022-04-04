#!usr/bin/env python

"""_summary_"""


import random

import tkinter as tk
from tkinter import ttk


# game_image = [ROCK, PAPER, SCISSORS]

# print("\nWelcome to the Rock, Paper, Scissors Game!\n")
# user_selection = int(
#     input("Please make your choice - Type 0 for Rock, 1 for Paper or 2 for Scissors...")
# )
# if user_selection < 0 or user_selection >= 3:
#     print("You typed an incorrect number - GAME OVER!")
# else:
#     print(game_image[user_selection])
#     cpu_selection = random.randint(0, 2)
#     print("\nThe computer chose...\n")
#     print(game_image[cpu_selection])
#     if user_selection == 0 and cpu_selection == 2:
#         print("\nYou Win!")
#     elif user_selection == 0 and cpu_selection == 0:
#         print("\nIt is a draw!")
#     elif user_selection == 0 and cpu_selection == 1:
#         print("\nYou Lose!")
#     elif user_selection == 1 and cpu_selection == 0:
#         print("\nYou Win!")
#     elif user_selection == 1 and cpu_selection == 1:
#         print("\nIt is a draw!")
#     elif user_selection == 1 and cpu_selection == 2:
#         print("\nYou Lose!")
#     elif user_selection == 2 and cpu_selection == 1:
#         print("\nYou Win!")
#     elif user_selection == 2 and cpu_selection == 2:
#         print("\nIt is a draw!")
#     elif user_selection == 2 and cpu_selection == 0:
#         print("\nYou Lose!")


class Gui:
    """[summary]"""

    def __init__(self, master):

        master.title("Rock, Paper, Scissors")
        master.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure("Header.TLabel", font=("Arial", 25, "bold"))

        self.header_frame = ttk.Frame(master, relief="ridge", padding=3)
        self.content_frame = ttk.Frame(master, padding=3)
        self.scores_frame = ttk.Frame(master, relief="ridge", padding=3)
        self.bottom_frame = ttk.Frame(master, padding=3)
        self.header_frame.grid(row=0)
        self.content_frame.grid(row=1)
        self.scores_frame.grid(row=2)
        self.bottom_frame.grid(row=3)

        self.game = tk.PhotoImage(file="game.png")
        self.rock = tk.PhotoImage(file="rock.png")
        self.paper = tk.PhotoImage(file="paper.png")
        self.scissors = tk.PhotoImage(file="scissors.png")

        ttk.Label(self.header_frame, image=self.game).grid(
            row=0, column=0, rowspan=2, padx=5, pady=5
        )
        ttk.Label(
            self.header_frame,
            text="Rock, Paper, Scissors Game",
            justify="center",
            style="Header.TLabel",
        ).grid(row=0, column=1, pady=5, sticky="s")
        ttk.Label(
            self.header_frame,
            text="by Kevin Banfield",
        ).grid(row=1, column=1, pady=5, sticky="n")
        ttk.Label(self.header_frame, image=self.game).grid(
            row=0, column=2, rowspan=2, padx=5, pady=5
        )

        ttk.Label(self.content_frame, text="Let's Play !", font=("Arial", 20)).grid(
            row=0, columnspan=5, pady=(10, 20)
        )

        ttk.Label(self.content_frame, text="Select Move:", font=("Arial", 16)).grid(
            row=2, column=0, padx=(61, 0), pady=(0, 5)
        )
        self.player_move = tk.StringVar(self.content_frame)
        ttk.Radiobutton(
            self.content_frame,
            text="Rock",
            variable=self.player_move,
            value="Rock",
            #            command=selection,
        ).grid(row=3, column=0, padx=(62, 0), sticky="w")
        ttk.Radiobutton(
            self.content_frame,
            text="Paper",
            variable=self.player_move,
            value="Paper",
            #            command=selection,
        ).grid(row=4, column=0, padx=(62, 0), sticky="w")
        ttk.Radiobutton(
            self.content_frame,
            text="Scissors",
            variable=self.player_move,
            value="Scissors",
            #            command=selection,
        ).grid(row=5, column=0, padx=(62, 0), sticky="w")

        ttk.Label(self.content_frame, image=self.rock).grid(
            row=2, column=1, rowspan=4, sticky="s", padx=40
        )

        ttk.Label(self.content_frame, text="V", font=("Arial", 24)).grid(
            row=3, column=2, rowspan=2
        )

        ttk.Label(self.content_frame, text="CPU Move    ", font=("Arial", 16)).grid(
            row=2, column=4, padx=(0, 62), pady=(0, 5)
        )

        ttk.Label(self.content_frame, image=self.rock).grid(
            row=2, column=3, rowspan=4, sticky="s", padx=40
        )
        ttk.Button(self.content_frame, text="Play").grid(row=6, columnspan=5, pady=10)

        self.winner = tk.Text(
            self.content_frame,
            width=15,
            height=3,
            font=("Arial", 18),
            foreground="green",
        )
        self.winner.grid(row=9, columnspan=5)

        ttk.Button(self.content_frame, text="Start Next Round").grid(
            row=10, columnspan=5, pady=10
        )

        ttk.Label(self.scores_frame, text="PLAYER WINS", font=("Arial", 16)).grid(
            row=0, column=0, padx=(5, 0), pady=(5, 10)
        )
        self.entry_player_wins = ttk.Entry(
            self.scores_frame, width=5, font=("Arial", 16)
        )
        self.entry_player_wins.grid(row=1, column=0, pady=(0, 10))
        ttk.Label(self.scores_frame, text=" CPU WINS  ", font=("Arial", 16)).grid(
            row=0, column=3, pady=(5, 10)
        )
        self.entry_cpu_wins = ttk.Entry(self.scores_frame, width=5, font=("Arial", 16))
        self.entry_cpu_wins.grid(row=1, column=3, pady=(0, 10))
        ttk.Button(self.scores_frame, text="Clear Scores").grid(
            row=0, column=1, rowspan=2, padx=(100, 120)
        )

        ttk.Button(self.bottom_frame, text="Quit Game").grid(row=0, column=0, pady=10)


#   def submit(self):


def main():
    """[summary]"""
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()


if __name__ == "__main__":
    main()


#        self.style = ttk.Style()
#        self.style.configure("TFrame", background="#e1d8b9")
#        self.style.configure("TButton", background="#e1d8b9")
#        self.style.configure("TLabel", background="#e1d8b9", font=("Arial", 11))
#        self.style.configure("Header.TLabel", font=("Arial", 18, "bold"))
