import random
import json

with open('words.json') as wordList:
  file_contents = wordList.read()

def errorMsg(enter): #@ defines a function for an error message
    if not enter.isalpha(): #Error message if word is not within alphabet
        print("The word must contain all letters, try again\n")
        enter = input("Choose a 5 letter word:")
        errorMsg(enter)
    if len(enter) != 5 :  # Error message if word is not 5 letters
        print("The word must be 5 characters, try again\n")
        enter = input("Choose a 5 letter word:")
        errorMsg(enter)
    if not enter in json.loads(file_contents):
        print("That is not a real word")
        enter = input("Choose a 5 letter word:")
        errorMsg(enter)
    return enter

def gameLoop():
    word = json.loads(file_contents)[random.randint(0, len(json.loads(file_contents)))]
    badGuess = []

    print("\nNow player enter a 5 letter word as a guess")
    guess = ""
    r = 0
    found = [False, False, False, False, False]
    while guess != word and r < 6:
        found = [False, False, False, False, False]
        guess = errorMsg(input("Enter a 5 letter word:"))

        for i in range(5): #runs this sequence once for each letter
            if guess[i] == word[i]: # if the guess is the same letter as the word print that
                print("The letter", guess[i], " in spot ", str(i + 1), "matches letter in correct spot")
                found[i] = True
            elif guess[i] != word[i]: #if the letter of the guess is not equal to the letter of the letter then check if yellow
                yellow = False
                for j in range(len(word)):
                    if guess[i] == word[j] and guess[j] != word[j] and found[j] == False:
                        #print("Found [j]", found[j], "j:", j)
                        print("The letter", guess[i], "is contained within the word")
                        yellow = True
                        found[j] = True
                        break
                if not yellow: # if it is not yellow
                    print("No Match")
                    if not guess[i] in badGuess:
                        badGuess.append(guess[i])
        print()
        print("The wrong letters are: ",badGuess)
        print(f"That was guess {r+1}")
        print()
        r += 1
    print(f"The word was {word}")
    print("Would you like to play again with a diffrent word (YES or NO)")
    answer = input("Answer:")
    if answer == "YES":
        gameLoop()

print("Welcome to wordle")
gameLoop()
