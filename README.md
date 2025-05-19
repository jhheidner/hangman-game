
🎮 Hangman Game (Tkinter GUI Edition)

A fun and interactive Hangman game built using Python's `tkinter` library for the graphical interface. This version uses modular components (`hangman_art.py` and `hangman_words.py`) to manage the ASCII art and word list separately for better organization and reuse.


🧩 Features

- ✅ Clean GUI interface built with `tkinter`
- 🔤 Button-based letter guessing (A–Z)
- 💀 Dynamic hangman ASCII art updates on incorrect guesses
- ❤️ Lives tracking and status feedback
- 🔁 Easy restart button to play again
- 🧠 Words randomly selected from a predefined list

---

🗂️ File Structure

hangman-gui/
├── hangman_gui.py         # Main game script (this file)
├── hangman_art.py         # ASCII art stages of the hangman
├── hangman_words.py       # List of words for the game
└── README.md              # Project description and instructions


🚀 How to Run

Requirements
- Python 3.x
- Tkinter (comes pre-installed with Python)

Steps

1. Clone the repository:

```bash
git clone https://github.com/jhheidner/hangman-gui.git
cd hangman-gui


2. Run the game:

```bash
python hangman_gui.py


🧱 Example `hangman_art.py`

```python
stages = [
    '''
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \
    |
    ''',
    # ... other stages ...
    '''
     _______
    |/      |
    |
    |
    |
    |
    |
    '''
]

📜 Example `hangman_words.py`

```python
word_list = [
    "aardvark", "baboon", "camel", "python", "flamingo", "zebra", "hangman"
]

🏁 Gameplay

- Click on a letter to guess.
- Correct guesses reveal their position(s).
- Incorrect guesses reduce your lives and draw the hangman.
- The game ends when you either guess the word or run out of lives.

👨‍💻 Author

- Developed by [@jhheidner](https://github.com/jhheidner)

📘 License

This project is free to use and modify for learning or personal use.
