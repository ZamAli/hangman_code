import random
from hangman_art import stages, logo
from hangman_words import word_list

word = random.choice(word_list)
print (word)
list_word = list(word)
# print (list_word)
lives = 6
guess_word_list = ["_"] * len(list_word)

while lives:
    user_letter = input("Enter a letter: ")
    if user_letter in list_word:
        for i in range(len(list_word)):
            if list_word[i] == user_letter:
                guess_word_list[i] = user_letter
        final_word = "".join(guess_word_list)
        print(final_word)
        if final_word == word:
            print (f"the word is {final_word}, you won!!!")
            break
    else:
        print (f"the letter {user_letter} does not exist in the word")
        print(guess_word_list)
        lives -=1
        print (f"you lost a live {lives}/6")
        if lives == 0:
            print("Game ended!! you couldn't save the life")
    print(stages[lives])
