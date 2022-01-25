# Wordle solver for 1/24/2022, World 219
import random 

# Read file with valid five letter words
with open("fiveLetterWords.txt", "r") as f:
    file = f.readlines()

# Old way was brute force, now I'm going to iterate over only valid words
letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'p', 'a', 's', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
words = []

# Just for converting strings
def convert(s):
    # initialization of string to ""
    str1 = ""
    # using join function join the list s by 
    # separating words by str1
    return(str1.join(s))

for word in file:
    if word.find('a') == 3 and word.find('u') == 1 and "i" not in word and "o" not in word and "d" not in word and "h" not in word and "n" not in word and "m" not in word:
        print(word)

