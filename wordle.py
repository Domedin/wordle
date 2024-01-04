def errorMsg(enter): #@ defines a function for an error message
    if not enter.isalpha(): #Error message if word is not within alphabet
        print("The word must contain all letters, try again\n")
        enter = input("Choose a 5 letter word:")
        errorMsg(enter)
    if len(enter) != 5 :  # Error message if word is not 5 letters
        print("The word must be 5 characters, try again\n")
        enter = input("Choose a 5 letter word:")
        errorMsg(enter)
        
print("Welcome to wordle")
print("The first player will choose a five letter word")
word = input("Choose a 5 letter word:")

errorMsg(word) #calls the error message

print("\nNow player 2 enter a 5 letter word as a guess")
guess = input("Enter a 5 letter word:")

errorMsg(guess) #calls the error message

for i in range(5):
    if guess[i] == word[i]:
        print("The letter", guess[i], "matches letter in correct spot")
    if guess[i] != word[i]:
        print("No Match")
        continue
    