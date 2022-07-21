import random
import string

from words import words

def get_valid_word(words):
    word = random.choice(words) #chooses a random word from the list
    while "-" in word or " " in word:
        word = random.choice(words)

        return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letter = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what letters have been guessed


user_input = input("Guess a letter: ").upper()
print(user_input)