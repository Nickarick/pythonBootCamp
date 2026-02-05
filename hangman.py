import random

word_list = ["aardvark", "baboon", "camel"]
correct_letters = [""]
chosen_word = random.choice(word_list)
print(chosen_word)

#placeholder for blanks

placeholder = ""

for guess in range(len(chosen_word)):
    placeholder += " _ "

print(placeholder)

#User enters letter until blanks are filled
game_over = False

while not game_over:

    guess = input("Guess a letter: \n").lower()
#Display that puts the letter in the right spot

    display = " "

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)

        elif letter in correct_letters:
            display += letter
        
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("you win")
