def errorMsg(enter): #@ defines a function for an error message
    if not enter.isalpha(): #Error message if word is not within alphabet
        print("The word must contain all letters, try again\n")
        enter = input("Choose a 5 letter word:")
        errorMsg(enter)
    if len(enter) != 5 :  # Error message if word is not 5 letters
        print("The word must be 5 characters, try again\n")
        enter = input("Choose a 5 letter word:")
        errorMsg(enter)
        
def gameLoop():
    print("The first player will choose a five letter word")
    word = input("Choose a 5 letter word:")

    errorMsg(word) #calls the error message

    print("\nNow player 2 enter a 5 letter word as a guess")
    guess = ""
    i = 0
    found = ["Not found", "Not found", "Not found", "Not found", "Not found"]
    while guess != word or i > 6:
        guess = input("Enter a 5 letter word:")
        errorMsg(guess) #calls the error message
        for i in range(5):
            if guess[i] == word[i]:
                print("The letter", guess[i], "matches letter in correct spot")
                found[i] = "Found"
            if guess[i] != word[i]:
                yellow = False
                for j in range(len(word)):
                    if guess[i] == word[j] and found[j] == "Not found":
                        print("The letter", guess[i], "is contained within the word")
                        yellow = True
                        found[j] = "Yellow"
                        break
                if not yellow:
                    print("No Match")
        i += 1

print("Welcome to wordle")
gameLoop()
print("Would you like to play again with a diffrent word (YES or NO)")
answer = input("Answer:")
if answer == "YES":
    gameLoop()