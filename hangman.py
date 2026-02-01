import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

#placeholder for blanks

placeholder = ""

for guess in range(len(chosen_word)):
    placeholder += " _ "

print(placeholder)

guess = input("Guess a letter: \n").lower()

#Display that puts the letter in the right spot

display = " "

for letter in chosen_word:
    if letter == guess:
        display = placeholder.replace("_", guess)
        print(display)
    else:
        print("Wrong")



#for letter in chosen_word:
