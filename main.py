# Wordle solver for 1/24/2022, World 219
import random 

# Read file with valid five letter words
with open("fiveLetterWords.txt", "r") as f:
    file = f.readlines()

letters = ['q', 't', 'o', 'f', 'h', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
words = []

# Just for converting strings
def convert(s):
    # initialization of string to ""
    str1 = ""
    # using join function join the list s by 
    # separating words by str1
    return(str1.join(s))

for a in range(2000):
    word = []
    for i in range(4):
        if i == 2: 
            word.append('o')
        if i == 3: 
            word.append('l\n')
        else:
            word.append(random.choice(letters))
    words.append(convert(word))

words = sorted(words)
print(*words)

#print(file)
for x in words:
    if x in file:
        print("FOUND: " + x)


