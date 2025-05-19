import random
import os
import hangman_words
import hangman_art

score_file = "hangman_scores.txt"

# ---------------- Leaderboard Function ----------------
def display_leaderboard(score_file):
    from collections import defaultdict

    scores = defaultdict(lambda: {"Wins": 0, "Losses": 0})

    if not os.path.exists(score_file):
        print("\nNo scores yet. Be the first to play!\n")
        return

    with open(score_file, "r") as file:
        for line in file:
            name, result = line.strip().split(",")
            if result == "Win":
                scores[name]["Wins"] += 1
            elif result == "Loss":
                scores[name]["Losses"] += 1

    print("\n===== Leaderboard =====")
    print("Player\tWins\tLosses")
    for player, record in scores.items():
        print(f"{player}\t{record['Wins']}\t{record['Losses']}")
    print("=======================\n")

# ---------------- Save Score Function ----------------
def save_score(name, result, score_file):
    with open(score_file, "a") as file:
        file.write(f"{name},{result}\n")

# ---------------- Main Game Function ----------------
def play_game(player_name):
    chosen_word = random.choice(hangman_words.word_list)
    word_length = len(chosen_word)
    lives = 6
    guessed_letters = []
    correct_letters = []
    game_over = False

    print(hangman_art.logo)
    print(f"The word has {word_length} letters.")

    display = ""
    for _ in range(word_length):
        display += "_"

    while not game_over:
        print(f"\n{lives} lives left.")
        print("Word: " + " ".join(display))

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print(f"Good guess! '{guess}' is in the word.")
            new_display = ""
            for i in range(word_length):
                if chosen_word[i] == guess or chosen_word[i] in correct_letters:
                    new_display += chosen_word[i]
                else:
                    new_display += display[i]
            display = new_display
            correct_letters.append(guess)
        else:
            lives -= 1
            print(f"'{guess}' is not in the word. You lose a life.")
            print(hangman_art.stages[lives])

        if "_" not in display:
            game_over = True
            print("\n🎉 You win! The word was:", chosen_word)
            save_score(player_name, "Win", score_file)

        if lives == 0:
            game_over = True
            print("\n💀 You lose! The word was:", chosen_word)
            save_score(player_name, "Loss", score_file)

# ---------------- Game Loop ----------------
def main():
    print("Welcome to Hangman!")
    player_name = input("Enter your name: ")

    rounds = int(input("How many rounds would you like to play? "))

    for round_num in range(1, rounds + 1):
        print(f"\n----- Round {round_num} of {rounds} -----")
        play_game(player_name)

    print("\nGame Over! Here's the leaderboard:")
    display_leaderboard(score_file)

if __name__ == "__main__":
    main()
