# Used to make api calls to PyDictionary
# Checks the submitted word,
#               returns true or false,
#               displays word and definition
import PyDictionary
from PyDictionary import PyDictionary
import sys, os


# def go_(word):
#     if PyDictionary(word).getMeanings() == {word: False}:
#         print("word doesn't exist")
#     else:
#         print(PyDictionary(word).getMeanings())


# The api force calls the print function when it fails, need to disable
# Disable
def block_print():
    sys.stdout = open(os.devnull, 'w')


# Restore
def enable_print():
    sys.stdout = sys.__stdout__


# calls the PyDictionary api
# returns the result
def spell_check(word):
    char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', '\\', ' ', "'", '(',
                 ')', '*', '+', ',', '-', '.', '/', ':', ';', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
    new_word = list(word)
    for x in new_word:
        if x in char_list:
            return False
    block_print()
    check = PyDictionary(word).getMeanings()
    enable_print()
    if check == {word: None}:
        return False
    else:
        return check


pass
