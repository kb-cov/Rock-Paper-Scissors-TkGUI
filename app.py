#!usr/bin/env python

"""_summary_"""


import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


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

        self.game = tk.PhotoImage(file="images/game.png")
        self.rock = tk.PhotoImage(file="images/rock.png")
        self.paper = tk.PhotoImage(file="images/paper.png")
        self.scissors = tk.PhotoImage(file="images/scissors.png")
        self.questionmark = tk.PhotoImage(file="images/questionmark.png")

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

        def player_selection():
            if self.player_move.get() == 0:
                ttk.Label(self.content_frame, image=self.rock).grid(
                    row=2, column=1, rowspan=4, sticky="s", padx=40
                )
            elif self.player_move.get() == 1:
                ttk.Label(self.content_frame, image=self.paper).grid(
                    row=2, column=1, rowspan=4, sticky="s", padx=40
                )
            elif self.player_move.get() == 2:
                ttk.Label(self.content_frame, image=self.scissors).grid(
                    row=2, column=1, rowspan=4, sticky="s", padx=40
                )

        self.player_move = tk.IntVar(self.content_frame)
        ttk.Radiobutton(
            self.content_frame,
            text="Rock",
            variable=self.player_move,
            value=0,
            command=player_selection,
        ).grid(row=3, column=0, padx=(62, 0), sticky="w")
        ttk.Radiobutton(
            self.content_frame,
            text="Paper",
            variable=self.player_move,
            value=1,
            command=player_selection,
        ).grid(row=4, column=0, padx=(62, 0), sticky="w")
        ttk.Radiobutton(
            self.content_frame,
            text="Scissors",
            variable=self.player_move,
            value=2,
            command=player_selection,
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

        self.win_count = tk.IntVar(value=0)
        self.loose_count = tk.IntVar(value=0)

        def win():
            self.winner.config(font=("Arial", 18), foreground="green", state=["normal"])
            self.winner.insert("1.0", "################")
            self.winner.insert("2.0", "##    YOU WIN    ##")
            self.winner.insert("3.0", "################")
            self.winner.config(state=["disabled"])
            self.win_count.set(self.win_count.get() + 1)
            self.entry_player_wins.config(state="normal")
            self.entry_player_wins.config(textvariable=self.win_count)
            self.entry_player_wins.config(state=["readonly"])

        def loose():
            self.winner.config(font=("Arial", 18), foreground="red", state=["normal"])
            self.winner.insert("1.0", "################")
            self.winner.insert("2.0", "## YOU LOOSE  ##")
            self.winner.insert("3.0", "################")
            self.winner.config(state=["disabled"])
            self.loose_count.set(self.loose_count.get() + 1)
            self.entry_cpu_wins.config(state="normal")
            self.entry_cpu_wins.config(textvariable=self.loose_count)
            self.entry_cpu_wins.config(state=["readonly"])

        def draw():
            self.winner.config(
                font=("Arial", 18), foreground="orange", state=["normal"]
            )
            self.winner.insert("1.0", "################")
            self.winner.insert("2.0", "##      DRAW      ##")
            self.winner.insert("3.0", "################")
            self.winner.config(state=["disabled"])

        def play():
            self.cpu_play = random.randint(0, 2)
            if self.cpu_play == 0:
                ttk.Label(self.content_frame, image=self.rock).grid(
                    row=2, column=3, rowspan=4, sticky="s", padx=40
                )
            elif self.cpu_play == 1:
                ttk.Label(self.content_frame, image=self.paper).grid(
                    row=2, column=3, rowspan=4, sticky="s", padx=40
                )
            elif self.cpu_play == 2:
                ttk.Label(self.content_frame, image=self.scissors).grid(
                    row=2, column=3, rowspan=4, sticky="s", padx=40
                )
            self.play.state(["disabled"])
            if self.player_move.get() == 0 and self.cpu_play == 2:
                win()
            elif self.player_move.get() == 0 and self.cpu_play == 0:
                draw()
            elif self.player_move.get() == 0 and self.cpu_play == 1:
                loose()
            elif self.player_move.get() == 1 and self.cpu_play == 0:
                win()
            elif self.player_move.get() == 1 and self.cpu_play == 1:
                draw()
            elif self.player_move.get() == 1 and self.cpu_play == 2:
                loose()
            elif self.player_move.get() == 2 and self.cpu_play == 1:
                win()
            elif self.player_move.get() == 2 and self.cpu_play == 2:
                draw()
            elif self.player_move.get() == 2 and self.cpu_play == 0:
                loose()

        ttk.Label(self.content_frame, image=self.questionmark).grid(
            row=2, column=3, rowspan=4, sticky="s", padx=40
        )

        self.play = ttk.Button(self.content_frame, text="Play", command=play)
        self.play.grid(row=6, columnspan=5, pady=10)

        self.winner = tk.Text(
            self.content_frame,
            width=15,
            height=3,
            font=("Arial", 18),
            foreground="green",
        )
        self.winner.grid(row=9, columnspan=5)

        def next_round():
            self.play.config(state=["normal"])
            self.winner.config(state=["normal"])
            self.winner.delete("1.0", "end")
            self.winner.config(state=["disabled"])
            ttk.Label(self.content_frame, image=self.questionmark).grid(
                row=2, column=3, rowspan=4, sticky="s", padx=40
            )

        self.next = ttk.Button(
            self.content_frame, text="Start Next Round", command=next_round
        )
        self.next.grid(row=10, columnspan=5, pady=10)

        ttk.Label(self.scores_frame, text="PLAYER WINS", font=("Arial", 16)).grid(
            row=0, column=0, padx=(5, 0), pady=(5, 10)
        )
        self.entry_player_wins = ttk.Entry(
            self.scores_frame,
            width=5,
            font=("Arial", 16),
            justify="center",
            state=["readonly"],
        )
        self.entry_player_wins.grid(row=1, column=0, pady=(0, 10))
        ttk.Label(self.scores_frame, text=" CPU WINS  ", font=("Arial", 16)).grid(
            row=0, column=3, pady=(5, 10)
        )
        self.entry_cpu_wins = ttk.Entry(
            self.scores_frame,
            width=5,
            font=("Arial", 16),
            justify="center",
            state=["readonly"],
        )
        self.entry_cpu_wins.grid(row=1, column=3, pady=(0, 10))

        def clear_scores():
            self.entry_cpu_wins.config(state="normal")
            self.entry_player_wins.config(state="normal")
            self.entry_cpu_wins.delete("0", "end")
            self.entry_player_wins.delete("0", "end")
            self.entry_cpu_wins.config(state=["readonly"])
            self.entry_player_wins.config(state=["readonly"])
            self.win_count = tk.IntVar(value=0)
            self.loose_count = tk.IntVar(value=0)

        ttk.Button(self.scores_frame, text="Clear Scores", command=clear_scores).grid(
            row=0, column=1, rowspan=2, padx=(100, 120)
        )

        def quit_game():
            self.exit = tk.messagebox.askquestion(title="Quit", message="Are you sure you want to quit ?")
            if self.exit == 'yes':
                master.destroy()
            else:
                tk.messagebox.showinfo('Return','You will now return to the game')

        ttk.Button(self.bottom_frame, text="Quit Game", command=quit_game).grid(row=0, column=0, pady=10)


def main():
    """[summary]"""
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
