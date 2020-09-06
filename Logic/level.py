import Dictionary
import Scramble
from Point import Point

__question = None
extra_list = []
word_list = []
word_found = []
definition = []


def game_over():
    print("----------------------------------------------------------------------------------------------------")
    print("Game Over")
    print_all("All")


def check_list(to_find, found):
    count = 0
    to_find_len = len(to_find)

    for x in found:
        if x in to_find:
            to_find.remove(x)
            count += 1

    if count == to_find_len:
        return True
    else:
        return False


def split(word, user_word):
    new_word = word.lower()
    new_user_word = user_word.lower()
    char_len = 0
    user_len = len(new_user_word)
    word_split = list(new_word)
    user_split = list(new_user_word)
    for x in user_split:
        if x in word_split:
            word_split.remove(x)
            char_len += 1

    if char_len == user_len:
        return True
    else:
        return False


def check_word_found(word):
    if word in word_found:
        print("You have already found this word \n")
        return True
    else:
        return False


def check_extra_word_found(word):
    if word in extra_list:
        print("You have already found this word \n")
        return True
    else:
        return False


# Prints everything the user has found throughout the level after the level ends
def print_all(level):
    print("----------------------------------------------------------------------------------------------------\n")
    print("Hurray you earned a total ", end="")
    print(Point.get_points(), "points :)", "\n")

    print("The words found are: ")
    for x in word_found:
        print(x)
    print()

    print("The extra word found are: ")
    if len(extra_list) is None:
        print("No extra elements were found \n")
    else:
        for z in extra_list:
            print(z)
        print()

    print("The definition of the words found are: ")
    for y in definition:
        print(y)
    print()

    print("----------------------------------------------------------------------------------------------------")
    if level == "All":
        print(f"{level} Levels Over")
    else:
        print(f"Level {level} Over")
    print("----------------------------------------------------------------------------------------------------")


def start(__question, word_list, level):
    question = __question.lower()
    lower_word_list = [each_word.lower() for each_word in word_list]

    print(f"Unscramble the word \"{question}\"")
    # The user has to enter a word with 3 letters or above
    # the user enters "_scramble_" to re-scramble the question
    print("Enter the word you can form from unscrambling the given word: "
          "and enter \"_scramble\" to re-scramble the question")

    # In this loop with the help of check_list() function we can get to know if all the words are found
    # when all the words are found it exits the loop
    # then it prints all the data collected
    while check_list(lower_word_list, word_found) is False:
        user_input = str(input()).lower()
        limit = len(user_input)

        # Checks if the user input is below the limit of 3 letters
        if limit <= 2:
            print("Enter a word with 3 letters or above \n")
            continue

        # User enters "_scramble_" to re-shuffle the question word
        if user_input == "_scramble":
            re_scramble = Scramble.word_scrambler(question)
            print(re_scramble, "\n")
            continue

        # checks if the characters in the user input exist in the question
        if split(question, user_input) is False:
            print("Please enter a word with the characters in the scrambled word \n")
            continue

        # gets the meaning of the word entered if the word exists
        check = Dictionary.spell_check(user_input)
        if check is not False:

            if user_input in lower_word_list:

                word_found.append(user_input)
                definition.append(check)
                Point.add_points()
                print("Word found \n")

            else:
                if check_word_found(user_input) is True:
                    continue
                elif check_extra_word_found(user_input) is True:
                    continue

                extra_list.append(user_input)
                definition.append(check)
                if len(extra_list) % 2 == 0:
                    Point.add_extra_points()
                print("Extra word \n")

        else:
            print("Word doesn't exist, try again \n")

    else:
        print_all(level)
