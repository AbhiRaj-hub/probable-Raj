import random
from Hangman_words import words

chosen_word = random.choice(words)
length = len(chosen_word)

end = False
lives = 6

from Hangman_logo import logo
print(logo)

display = []
for _ in range(length):
    display += "_"

while not end:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print("Wrong!")
        lives -= 1
        if lives == 0:
            end = True
            print("You lose!")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from Hangman_logo import stages
    print(stages[lives])

