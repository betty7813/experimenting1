import random
import string
from words import words

def get_valid_word(words):
    word=random.choice(words) 
    while "-" or " " in word:
        word=random.choice(words)
    return word

def hangman():
    word=get_valid_word(words)
    word_letters=set(word)  #letters in the word
    alphabet=set(string.ascii_uppercase)
    used_letters=set() #what the user guessed 

    #getting user input
  while len(word_letters)>0:
    user_letter=input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:
        used_leters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print("You have already used that character. Please try again!")

    else:
        print("Invalid character")

user_input = input("Type something:")



    

