
#Roll Number : TECOA119
#Name : Pragati Rajesh Chothe

import random
print("***** HANGMAN GAME *******")

Words = ["apple","banana","Mango","Cherry","pineapple","strawberry","orange","watermelon","kiwi","chikoo"]

chances = 5

randomword = random.choice(Words)

print("HINT:")
print(randomword[0:1])
print(randomword[4:5])
print("length of randomword is =",len(randomword))

guesses=" "

while chances > 0:
    failed = 0

    for char in randomword:
        if char in guesses:
            print(char)

        else:
            print("_")
            failed += 1

    if failed == 0:
        print(" Congratulation!!!! You Won")
        print("The word is: ", randomword)
        break

    guess = input("guess a character:")
    guesses += guess

    if guess not in randomword:
        chances -= 1
        print("You have guess a wrong character, you've lost a chance")

        if chances == 0:
            print("Sorry! you lost the game. Try Again....!")