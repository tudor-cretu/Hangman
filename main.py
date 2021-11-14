import random
import string
from words import words
from visual import lives_visual_dict

def get_valid_word(words):
    word = random.choice(words) # randomly chooses a word
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what user has guessed
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        # letters used
        print("You have used these letters:", " ".join(used_letters))
        print("You have", lives, "lives left!")

        # what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print("Current word: ", " ".join(word_list))
        # getting user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in word")
        elif user_letter in used_letters:
            print("You have aleardy used that character. Please try again.")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print(lives_visual_dict[lives])
        print("You died, sorry. The word was", word)
    else:
        print("You guessed the word,", word + '!')
        print("You have", lives, "left!")

hangman()