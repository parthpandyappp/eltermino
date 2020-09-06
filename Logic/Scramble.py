# Generates Random char sequence
# The Grabs a random word within a set char length to use as the base
# The char length is based on a difficulty setting
import random

# Shuffles the word in place
def WordScrambler(word):
    listWord = list(word)
    random.shuffle(listWord)
    result = ''.join(listWord)
    return result

