import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

#placeholder for blanks

placeholder = ""

for guess in range(len(chosen_word)):
    placeholder += " _ "

print(placeholder)

display = ""
while chosen_word == display:
    guess = input("Guess a letter: \n").lower()
    for letter in chosen_word:
        if letter == guess:
            display += letter   
        else:
            display += "_"

print(display)


#for letter in chosen_word:
