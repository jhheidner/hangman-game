import tkinter as tk
import random
import hangman_art
import hangman_words

# Word list
word_list = hangman_words.word_list

# Main Game Class
class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.reset_game()

    def reset_game(self):
        self.word = random.choice(word_list)
        self.display_word = ["_" for _ in self.word]
        self.guessed_letters = set()
        self.lives = 6

        self.build_gui()

    def build_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.label_word = tk.Label(self.root, text=" ".join(self.display_word), font=("Courier", 24))
        self.label_word.pack(pady=10)

        self.label_hangman = tk.Label(self.root, text=hangman_art.stages[6], font=("Courier", 12), justify="left")
        self.label_hangman.pack()

        self.label_status = tk.Label(self.root, text=f"Lives left: {self.lives}", font=("Arial", 14))
        self.label_status.pack(pady=5)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
            btn = tk.Button(self.buttons_frame, text=letter.upper(), width=4, font=("Arial", 12),
                            command=lambda l=letter: self.make_guess(l))
            btn.grid(row=i // 9, column=i % 9, padx=2, pady=2)

        self.restart_button = tk.Button(self.root, text="Restart", font=("Arial", 12), command=self.reset_game)
        self.restart_button.pack(pady=10)

    def make_guess(self, letter):
        if letter in self.guessed_letters:
            return

        self.guessed_letters.add(letter)

        if letter in self.word:
            for idx, char in enumerate(self.word):
                if char == letter:
                    self.display_word[idx] = letter
        else:
            self.lives -= 1

        self.update_ui()

    def update_ui(self):
        self.label_word.config(text=" ".join(self.display_word))
        self.label_status.config(text=f"Lives left: {self.lives}")
        self.label_hangman.config(text=hangman_art.stages[self.lives])  # <- FIXED

        if "_" not in self.display_word:
            self.label_status.config(text="🎉 You Win!")
            self.disable_buttons()
        elif self.lives == 0:
            self.label_status.config(text=f"💀 You Lose! Word was '{self.word}'")
            self.label_word.config(text=" ".join(self.word))
            self.disable_buttons()

    def disable_buttons(self):
        for child in self.buttons_frame.winfo_children():
            child.config(state="disabled")

# Run the game
root = tk.Tk()
game = HangmanGame(root)
root.mainloop()
