import random 

print("\n***** HANGMAN GAME *******")

HANGMAN = ('''

   +---+
   |   |
       |
       |
       |
       |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+c
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')


Words = ["apple","banana","Mango","Cherry","pineapple","strawberry","orange","watermelon","kiwi","chikoo","chairs", "backpack", "bodywash", "clothing", "computer", "python", "program", "glasses",
         "sweatshirt", "sweatpants", "mattress", "friends", "clocks", "biology", "algebra", "suitcase", "knives",
         "ninjas", "shampoo", "chemistry", "sololearn", "bottle", "physics"]

def prCyan(randomletter): 
    #Print Color Word
    print("\033[96m {}\033[00m" .format(randomletter))

def displayBoard(HANGMAN, wrongchoice, correctchoice, randomword):
    print(HANGMAN[len(wrongchoice)])
    print()

    print("Guess Wrong Characters : ", end=' ')
    for letter in wrongchoice:
        print(letter, end=' ')
    print()

    blanks = '_' * len(randomword)

    for i in range(len(randomword)):                                # replace blanks with correctly guessed letters
        if randomword[i] in correctchoice:
            blanks = blanks[:i] + randomword[i] + blanks[i+1:]

    for letter in blanks:                                           # show the random word with spaces in between each letter
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    # This function makes sure the player entered a single letter, and not something else.
    while True:
        guess = input("Guess a character: ")
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a LETTER.")
        else:
            return guess

         
wrongchoice = ''
correctchoice = ''
randomword = random.choice(Words)
gameIsDone = False

print("\nHINT:")
print(randomword[0:1])
print(randomword[4:5])
print("length of randomword is =",len(randomword))

while True :
    displayBoard(HANGMAN, wrongchoice, correctchoice, randomword)
    guess = getGuess(wrongchoice + correctchoice)
    
    if guess in randomword:
        correctchoice = correctchoice + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(randomword)):
            if randomword[i] not in correctchoice:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(" Congratulation!!!! You Won.... :) \n" + "Yes the Correct Word is ")
            prCyan(randomword)
            gameIsDone = True
    else:
        wrongchoice = wrongchoice + guess

        # Check if player has guessed too many times and lost.
        if len(wrongchoice) == len(HANGMAN) - 1:
            displayBoard(HANGMAN, wrongchoice, correctchoice, randomword)
            print("You have run out of guesses!\nAfter " + str(len(wrongchoice)) + " missed guesses and " + str(len(correctchoice)) + " correct guesses, the word was " )
            prCyan(randomword)
            gameIsDone = True

    # Ask the player if they want to play again.
    if gameIsDone:
        playAgain=input("Do you want to play again? (yes or no) : ")
        if playAgain=='Yes' or playAgain=='yes':
            wrongchoice = ''
            correctchoice = ''
            gameIsDone = False
            randomword = random.choice(Words) 
            
            print("\nHINT:")
            print(randomword[0:1])
            print(randomword[4:5])
            print("length of randomword is =",len(randomword))  
        else:
           break
