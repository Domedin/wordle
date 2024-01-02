from random import *

print("Welcome to wordle")
print("The first player will choose a five letter word")
word = input("Choose a 5 letter word:")

while not word.isalpha():
    print("The word must contain all letters")
    word = input("Choose a 5 letter word:")
while len(word) > 5 or len(word) < 5:
    print("The word must be 5 characters")
    word = input("Choose a 5 letter word:")

print(word)