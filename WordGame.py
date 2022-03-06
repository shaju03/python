words_list = ["apple","book","cat","dog","elephant","fish"]

import random
choosen_word = random.choice(words_list)
word_len = len(choosen_word)
blank = []
for _ in range(word_len):
    blank += "_"
print(blank)
end_game = False
while not end_game:
    user_guess = input("choose the letter: ")
    for position in range(word_len):
        letter = choosen_word[position]
        if letter == user_guess:
            blank[position] = letter
    print(blank)
    if "_" not in blank:
        end_game = True
print("you win..")


