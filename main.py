#12972 possible words
#10657 guess words
#2315 valid words 

# Wordle solver

# Stage 1: Have it successfully guess a word given certain parameters - COMPLETE
# Stage 2: Have it interpret what the most common letters in 5 letter words are (use list from english word list) - IN PROCESS
# Stage 3: Clean up code, make it more modular
# Stage 4: Have it fully autonomous and hooked up to online, guessing itself

from wordleDict import validWords

possibleWords = []
i = 0        
for word in validWords:
    if 'l' in word and word.find('o') == 1 and word.find('u') == 2 and 'a' not in word and 't' not in word and 'e' not in word and 'e' not in word and 'r' not in word:
        possibleWords.append(word)
        i+=1

print(*sorted(possibleWords))
print("Possible words: ", i)
