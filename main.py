#12972 possible words
#10657 guess words
#2315 valid words 

# Wordle solver

# Stage 1: Have it successfully guess a word given certain parameters - COMPLETE
# Stage 2: Have it interpret what the most common letters in 5 letter words are (use list from english word list) - IN PROCESS
# Stage 3: Clean up code, make it more modular
# Stage 4: Have it fully autonomous and hooked up to online, guessing itself

from wordleDict import validWords
        
print(*validWords)
print("Possible words: ", len(validWords))
