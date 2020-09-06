from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
from .forms import levelone
from PyDictionary import PyDictionary
import random

class Point:
    _points = 0

    @classmethod
    def add_extra_points(cls):
        cls._points += 1
        print("You earned 1 point for 2 extra words")

    @classmethod
    def add_points(cls):
        cls._points += 2
        print("You earned 2 points for every valid word")

    @classmethod
    def get_points(cls):
        return cls._points


extra_list = []
word_found = []
definition = []


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
        # print("You have already found this word \n")
        return True
    else:
        return False


def check_extra_word_found(word):
    if word in extra_list:
        return True
    else:
        return False


def spell_check(word):
    char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', '\\', ' ', "'", '(',
                 ')', '*', '+', ',', '-', '.', '/', ':', ';', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
    new_word = list(word)
    for x in new_word:
        if x in char_list:
            return False
    #block_print()
    check = PyDictionary(word).getMeanings()
    #enable_print()
    if check == {word: None}:
        return False
    else:
        return check


def WordScrambler(word):
    listWord = list(word)
    random.shuffle(listWord)
    result = ''.join(listWord)
    return result


def index(request):
    if request.user.is_authenticated:
        pass
    else:
        messages.info(
            request, "You must be Signed-up or Login to play the game")
    return render(request, "term/index.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/user-registration.html', context)


def levels(request):
    return render(request, "term/level.html")

def ins(request):
    return render(request, "term/instructions.html")

def level1(request):
    question="datoy"
    word_list = ["today", "toady", "toad", "toy", "tad"]
    if request.method == 'POST':
        form = levelone(request.POST)

        if form.is_valid():
            while check_list(word_list, word_found) is False:
                user_input = str(form.cleaned_data['Word']).lower()
                limit = len(user_input)

                if limit <= 2:
                    messages.info(request,"Please enter a word with 3 characters or above.")
                    return redirect('level1')

                if user_input == "_scramble":
                    re_scramble = WordScrambler(question)
                    question = re_scramble
                    messages.info(request,"Your question has been re_scrambled")
                    return render(request, "term/level1.html",{'form':form, 'que':question})

                if split(question, user_input) is False:
                    messages.info(request,"Please enter a word with the characters in the scrambled word")
                    return redirect('level1')

                check = spell_check(user_input)
                if check is not False:
                    if user_input in word_list:
                        word_found.append(user_input)
                        definition.append(check)
                        Point.add_points()
                        messages.info(request,"You earned 2 points for every valid word.")
                        messages.info(request, "Congrats, Word Found!")
                        return redirect('level1')
                    else:
                        if check_word_found(user_input) is True:
                            messages.info(request,"You have already found this word")
                            return redirect('level1')
                        elif check_extra_word_found(user_input) is True:
                            messages.info(request, "You have already found this word")
                            return redirect('level1')

                        extra_list.append(user_input)
                        definition.append(check)
                        Point.add_extra_points()
                        if len(extra_list) % 2 == 0:
                            messages.info(request,"You earned 1 Point for 2 extra words")
                        messages.info(request, "Congrats, Extra Word Found!")
                        return redirect('level1')
                else:
                    messages.info(request, "Word doesn't exist, try again \n")
                    return redirect('level1')
            else:
                messages.info(request, "You have finished the level")
                # context={'form':form, 'que':question}
                # return render(request, "term/level1.html", context)
                context = {'word':word_found, 'extra':extra_list, 'def':definition}
                return render(request,"term/done.html", context)
    else:
        form = levelone()
    context={'form':form, 'que':question, 'point':Point.get_points(), 'lev':"Level 1"}
    return render(request, "term/level1.html", context)


def level2(request):
    question="igyleln"
    word_list = ["yelling", "eying", "lying", "glen", "lien"]
    if request.method == 'POST':
        form = levelone(request.POST)

        if form.is_valid():
            while check_list(word_list, word_found) is False:
                user_input = str(form.cleaned_data['Word']).lower()
                limit = len(user_input)

                if limit <= 2:
                    messages.info(request,"Please enter a word with 3 characters or above.")
                    return redirect('level2')

                if user_input == "_scramble":
                    re_scramble = WordScrambler(question)
                    question = re_scramble
                    messages.info(request,"Your question has been re_scrambled")
                    return render(request, "term/level2.html",{'form':form, 'que':question})

                if split(question, user_input) is False:
                    messages.info(request,"Please enter a word with the characters in the scrambled word")
                    return redirect('level2')

                check = spell_check(user_input)
                if check is not False:
                    if user_input in word_list:
                        word_found.append(user_input)
                        definition.append(check)
                        Point.add_points()
                        messages.info(request,"You earned 2 points for every valid word.")
                        messages.info(request, "Congrats, Word Found!")
                        return redirect('level2')
                    else:
                        if check_word_found(user_input) is True:
                            messages.info(request,"You have already found this word")
                            return redirect('level2')
                        elif check_extra_word_found(user_input) is True:
                            messages.info(request, "You have already found this word")
                            return redirect('level2')

                        extra_list.append(user_input)
                        definition.append(check)
                        Point.add_extra_points()
                        if len(extra_list) % 2 == 0:
                            messages.info(request,"You earned 1 Point for 2 extra words")
                        messages.info(request, "Congrats, Extra Word Found!")
                        return redirect('level2')
                else:
                    messages.info(request, "Word doesn't exist, try again \n")
                    return redirect('level2')
            else:
                messages.info(request, "You have finished the level")
                # context={'form':form, 'que':question}
                # return render(request, "term/level1.html", context)
                context = {'word':word_found, 'extra':extra_list, 'def':definition}
                return render(request,"term/done.html", context)
    else:
        form = levelone()
    context={'form':form, 'que':question, 'point':Point.get_points()}
    return render(request, "term/level2.html", context)


def level3(request):
    question = "irifgd"
    word_list = ["frigid", "rigid", "grid", "gird", "rig"]
    if request.method == 'POST':
        form = levelone(request.POST)

        if form.is_valid():
            while check_list(word_list, word_found) is False:
                user_input = str(form.cleaned_data['Word']).lower()
                limit = len(user_input)

                if limit <= 2:
                    messages.info(request,"Please enter a word with 3 characters or above.")
                    return redirect('level3')

                if user_input == "_scramble":
                    re_scramble = WordScrambler(question)
                    question = re_scramble
                    messages.info(request,"Your question has been re_scrambled")
                    return render(request, "term/level3.html",{'form':form, 'que':question})

                if split(question, user_input) is False:
                    messages.info(request,"Please enter a word with the characters in the scrambled word")
                    return redirect('level3')

                check = spell_check(user_input)
                if check is not False:
                    if user_input in word_list:
                        word_found.append(user_input)
                        definition.append(check)
                        Point.add_points()
                        messages.info(request,"You earned 2 points for every valid word.")
                        messages.info(request, "Congrats, Word Found!")
                        return redirect('level3')
                    else:
                        if check_word_found(user_input) is True:
                            messages.info(request,"You have already found this word")
                            return redirect('level3')
                        elif check_extra_word_found(user_input) is True:
                            messages.info(request, "You have already found this word")
                            return redirect('level3')

                        extra_list.append(user_input)
                        definition.append(check)
                        Point.add_extra_points()
                        if len(extra_list) % 2 == 0:
                            messages.info(request,"You earned 1 Point for 2 extra words")
                        messages.info(request, "Congrats, Extra Word Found!")
                        return redirect('level3')
                else:
                    messages.info(request, "Word doesn't exist, try again \n")
                    return redirect('level3')
            else:
                messages.info(request, "You have finished the level")
                # context={'form':form, 'que':question}
                # return render(request, "term/level1.html", context)
                context = {'word':word_found, 'extra':extra_list, 'def':definition}
                return render(request,"term/done.html", context)
    else:
        form = levelone()
    context={'form':form, 'que':question, 'point':Point.get_points()}
    return render(request, "term/level3.html", context)


def level4(request):
    question = "teerh"
    word_list = ["there", "three", "ether", "here", "tee"]
    if request.method == 'POST':
        form = levelone(request.POST)

        if form.is_valid():
            while check_list(word_list, word_found) is False:
                user_input = str(form.cleaned_data['Word']).lower()
                limit = len(user_input)

                if limit <= 2:
                    messages.info(request,"Please enter a word with 3 characters or above.")
                    return redirect('level4')

                if user_input == "_scramble":
                    re_scramble = WordScrambler(question)
                    question = re_scramble
                    messages.info(request,"Your question has been re_scrambled")
                    return render(request, "term/level4.html",{'form':form, 'que':question})

                if split(question, user_input) is False:
                    messages.info(request,"Please enter a word with the characters in the scrambled word")
                    return redirect('level4')

                check = spell_check(user_input)
                if check is not False:
                    if user_input in word_list:
                        word_found.append(user_input)
                        definition.append(check)
                        Point.add_points()
                        messages.info(request,"You earned 2 points for every valid word.")
                        messages.info(request, "Congrats, Word Found!")
                        return redirect('level4')
                    else:
                        if check_word_found(user_input) is True:
                            messages.info(request,"You have already found this word")
                            return redirect('level4')
                        elif check_extra_word_found(user_input) is True:
                            messages.info(request, "You have already found this word")
                            return redirect('level4')

                        extra_list.append(user_input)
                        definition.append(check)
                        Point.add_extra_points()
                        if len(extra_list) % 2 == 0:
                            messages.info(request,"You earned 1 Point for 2 extra words")
                        messages.info(request, "Congrats, Extra Word Found!")
                        return redirect('level4')
                else:
                    messages.info(request, "Word doesn't exist, try again \n")
                    return redirect('level4')
            else:
                messages.info(request, "You have finished the level")
                # context={'form':form, 'que':question}
                # return render(request, "term/level1.html", context)
                context = {'word':word_found, 'extra':extra_list, 'def':definition}
                return render(request,"term/done.html", context)
    else:
        form = levelone()
    context={'form':form, 'que':question, 'point':Point.get_points()}
    return render(request, "term/level4.html", context)


def level5(request):
    question = "voiinl"
    word_list = ["violin", "lion", "loin", "oil", "nil"]
    if request.method == 'POST':
        form = levelone(request.POST)

        if form.is_valid():
            while check_list(word_list, word_found) is False:
                user_input = str(form.cleaned_data['Word']).lower()
                limit = len(user_input)

                if limit <= 2:
                    messages.info(request,"Please enter a word with 3 characters or above.")
                    return redirect('level5')

                if user_input == "_scramble":
                    re_scramble = WordScrambler(question)
                    question = re_scramble
                    messages.info(request,"Your question has been re_scrambled")
                    return render(request, "term/level5.html",{'form':form, 'que':question})

                if split(question, user_input) is False:
                    messages.info(request,"Please enter a word with the characters in the scrambled word")
                    return redirect('level5')

                check = spell_check(user_input)
                if check is not False:
                    if user_input in word_list:
                        word_found.append(user_input)
                        definition.append(check)
                        Point.add_points()
                        messages.info(request,"You earned 2 points for every valid word.")
                        messages.info(request, "Congrats, Word Found!")
                        return redirect('level5')
                    else:
                        if check_word_found(user_input) is True:
                            messages.info(request,"You have already found this word")
                            return redirect('level5')
                        elif check_extra_word_found(user_input) is True:
                            messages.info(request, "You have already found this word")
                            return redirect('level5')

                        extra_list.append(user_input)
                        definition.append(check)
                        Point.add_extra_points()
                        if len(extra_list) % 2 == 0:
                            messages.info(request,"You earned 1 Point for 2 extra words")
                        messages.info(request, "Congrats, Extra Word Found!")
                        return redirect('level5')
                else:
                    messages.info(request, "Word doesn't exist, try again \n")
                    return redirect('level5')
            else:
                messages.info(request, "You have finished the level")
                # context={'form':form, 'que':question}
                # return render(request, "term/level1.html", context)
                context = {'word':word_found, 'extra':extra_list, 'def':definition}
                return render(request,"term/done.html", context)
    else:
        form = levelone()
    context={'form':form, 'que':question, 'point':Point.get_points()}
    return render(request, "term/level5.html", context)


def level6(request):
    question = "mmeiud"
    word_list = ["medium", "mime", "dime", "die", "med"]
    if request.method == 'POST':
        form = levelone(request.POST)

        if form.is_valid():
            while check_list(word_list, word_found) is False:
                user_input = str(form.cleaned_data['Word']).lower()
                limit = len(user_input)

                if limit <= 2:
                    messages.info(request,"Please enter a word with 3 characters or above.")
                    return redirect('level6')

                if user_input == "_scramble":
                    re_scramble = WordScrambler(question)
                    question = re_scramble
                    messages.info(request,"Your question has been re_scrambled")
                    return render(request, "term/leve6.html",{'form':form, 'que':question})

                if split(question, user_input) is False:
                    messages.info(request,"Please enter a word with the characters in the scrambled word")
                    return redirect('level6')

                check = spell_check(user_input)
                if check is not False:
                    if user_input in word_list:
                        word_found.append(user_input)
                        definition.append(check)
                        Point.add_points()
                        messages.info(request,"You earned 2 points for every valid word.")
                        messages.info(request, "Congrats, Word Found!")
                        return redirect('level6')
                    else:
                        if check_word_found(user_input) is True:
                            messages.info(request,"You have already found this word")
                            return redirect('level6')
                        elif check_extra_word_found(user_input) is True:
                            messages.info(request, "You have already found this word")
                            return redirect('level6')

                        extra_list.append(user_input)
                        definition.append(check)
                        Point.add_extra_points()
                        if len(extra_list) % 2 == 0:
                            messages.info(request,"You earned 1 Point for 2 extra words")
                        messages.info(request, "Congrats, Extra Word Found!")
                        return redirect('level6')
                else:
                    messages.info(request, "Word doesn't exist, try again \n")
                    return redirect('level6')
            else:
                messages.info(request, "You have finished the level")
                # context={'form':form, 'que':question}
                # return render(request, "term/level1.html", context)
                context = {'word':word_found, 'extra':extra_list, 'def':definition}
                return render(request,"term/done.html", context)
    else:
        form = levelone()
    context={'form':form, 'que':question, 'point':Point.get_points()}
    return render(request, "term/level6.html", context)


def level7(request):
    question = "neozd"
    word_list = ["dozen", "zone", "node", "doze", "eon"]
    if request.method == 'POST':
        form = levelone(request.POST)

        if form.is_valid():
            while check_list(word_list, word_found) is False:
                user_input = str(form.cleaned_data['Word']).lower()
                limit = len(user_input)

                if limit <= 2:
                    messages.info(request,"Please enter a word with 3 characters or above.")
                    return redirect('level7')

                if user_input == "_scramble":
                    re_scramble = WordScrambler(question)
                    question = re_scramble
                    messages.info(request,"Your question has been re_scrambled")
                    return render(request, "term/level7.html",{'form':form, 'que':question})

                if split(question, user_input) is False:
                    messages.info(request,"Please enter a word with the characters in the scrambled word")
                    return redirect('level7')

                check = spell_check(user_input)
                if check is not False:
                    if user_input in word_list:
                        word_found.append(user_input)
                        definition.append(check)
                        Point.add_points()
                        messages.info(request,"You earned 2 points for every valid word.")
                        messages.info(request, "Congrats, Word Found!")
                        return redirect('level7')
                    else:
                        if check_word_found(user_input) is True:
                            messages.info(request,"You have already found this word")
                            return redirect('level7')
                        elif check_extra_word_found(user_input) is True:
                            messages.info(request, "You have already found this word")
                            return redirect('level7')

                        extra_list.append(user_input)
                        definition.append(check)
                        Point.add_extra_points()
                        if len(extra_list) % 2 == 0:
                            messages.info(request,"You earned 1 Point for 2 extra words")
                        messages.info(request, "Congrats, Extra Word Found!")
                        return redirect('level7')
                else:
                    messages.info(request, "Word doesn't exist, try again \n")
                    return redirect('level7')
            else:
                messages.info(request, "You have finished the level")
                # context={'form':form, 'que':question}
                # return render(request, "term/level1.html", context)
                context = {'word':word_found, 'extra':extra_list, 'def':definition}
                return render(request,"term/done.html", context)
    else:
        form = levelone()
    context={'form':form, 'que':question, 'point':Point.get_points()}
    return render(request, "term/level7.html", context)


def level8(request):
    question = "jnleug"
    word_list = ["jungle", "lunge", "lung", "glue", "june"]
    if request.method == 'POST':
        form = levelone(request.POST)

        if form.is_valid():
            while check_list(word_list, word_found) is False:
                user_input = str(form.cleaned_data['Word']).lower()
                limit = len(user_input)

                if limit <= 2:
                    messages.info(request,"Please enter a word with 3 characters or above.")
                    return redirect('level8')

                if user_input == "_scramble":
                    re_scramble = WordScrambler(question)
                    question = re_scramble
                    messages.info(request,"Your question has been re_scrambled")
                    return render(request, "term/level8.html",{'form':form, 'que':question})

                if split(question, user_input) is False:
                    messages.info(request,"Please enter a word with the characters in the scrambled word")
                    return redirect('level8')

                check = spell_check(user_input)
                if check is not False:
                    if user_input in word_list:
                        word_found.append(user_input)
                        definition.append(check)
                        Point.add_points()
                        messages.info(request,"You earned 2 points for every valid word.")
                        messages.info(request, "Congrats, Word Found!")
                        return redirect('level8')
                    else:
                        if check_word_found(user_input) is True:
                            messages.info(request,"You have already found this word")
                            return redirect('level8')
                        elif check_extra_word_found(user_input) is True:
                            messages.info(request, "You have already found this word")
                            return redirect('level8')

                        extra_list.append(user_input)
                        definition.append(check)
                        Point.add_extra_points()
                        if len(extra_list) % 2 == 0:
                            messages.info(request,"You earned 1 Point for 2 extra words")
                        messages.info(request, "Congrats, Extra Word Found!")
                        return redirect('level8')
                else:
                    messages.info(request, "Word doesn't exist, try again \n")
                    return redirect('level8')
            else:
                messages.info(request, "You have finished the level")
                # context={'form':form, 'que':question}
                # return render(request, "term/level1.html", context)
                context = {'word':word_found, 'extra':extra_list, 'def':definition}
                return render(request,"term/done.html", context)
    else:
        form = levelone()
    context={'form':form, 'que':question, 'point':Point.get_points()}
    return render(request, "term/level8.html", context)


def level9(request):
    question = "pclbiu"
    word_list = ["public", "picul", "blip", "cub", "lip"]
    if request.method == 'POST':
        form = levelone(request.POST)

        if form.is_valid():
            while check_list(word_list, word_found) is False:
                user_input = str(form.cleaned_data['Word']).lower()
                limit = len(user_input)

                if limit <= 2:
                    messages.info(request,"Please enter a word with 3 characters or above.")
                    return redirect('level9')

                if user_input == "_scramble":
                    re_scramble = WordScrambler(question)
                    question = re_scramble
                    messages.info(request,"Your question has been re_scrambled")
                    return render(request, "term/level9.html",{'form':form, 'que':question})

                if split(question, user_input) is False:
                    messages.info(request,"Please enter a word with the characters in the scrambled word")
                    return redirect('level9')

                check = spell_check(user_input)
                if check is not False:
                    if user_input in word_list:
                        word_found.append(user_input)
                        definition.append(check)
                        Point.add_points()
                        messages.info(request,"You earned 2 points for every valid word.")
                        messages.info(request, "Congrats, Word Found!")
                        return redirect('level9')
                    else:
                        if check_word_found(user_input) is True:
                            messages.info(request,"You have already found this word")
                            return redirect('level9')
                        elif check_extra_word_found(user_input) is True:
                            messages.info(request, "You have already found this word")
                            return redirect('level9')

                        extra_list.append(user_input)
                        definition.append(check)
                        Point.add_extra_points()
                        if len(extra_list) % 2 == 0:
                            messages.info(request,"You earned 1 Point for 2 extra words")
                        messages.info(request, "Congrats, Extra Word Found!")
                        return redirect('level9')
                else:
                    messages.info(request, "Word doesn't exist, try again \n")
                    return redirect('level9')
            else:
                messages.info(request, "You have finished the level")
                # context={'form':form, 'que':question}
                # return render(request, "term/level1.html", context)
                context = {'word':word_found, 'extra':extra_list, 'def':definition}
                return render(request,"term/done.html", context)
    else:
        form = levelone()
    context={'form':form, 'que':question, 'point':Point.get_points()}
    return render(request, "term/level9.html", context)


def level10(request):
    question = "bcutcka"
    word_list = ["cutback", "buck", "tuba", "tack", "tab"]
    if request.method == 'POST':
        form = levelone(request.POST)

        if form.is_valid():
            while check_list(word_list, word_found) is False:
                user_input = str(form.cleaned_data['Word']).lower()
                limit = len(user_input)

                if limit <= 2:
                    messages.info(request,"Please enter a word with 3 characters or above.")
                    return redirect('level10')

                if user_input == "_scramble":
                    re_scramble = WordScrambler(question)
                    question = re_scramble
                    messages.info(request,"Your question has been re_scrambled")
                    return render(request, "term/level10.html",{'form':form, 'que':question})

                if split(question, user_input) is False:
                    messages.info(request,"Please enter a word with the characters in the scrambled word")
                    return redirect('level10')

                check = spell_check(user_input)
                if check is not False:
                    if user_input in word_list:
                        word_found.append(user_input)
                        definition.append(check)
                        Point.add_points()
                        messages.info(request,"You earned 2 points for every valid word.")
                        messages.info(request, "Congrats, Word Found!")
                        return redirect('level10')
                    else:
                        if check_word_found(user_input) is True:
                            messages.info(request,"You have already found this word")
                            return redirect('level10')
                        elif check_extra_word_found(user_input) is True:
                            messages.info(request, "You have already found this word")
                            return redirect('level10')

                        extra_list.append(user_input)
                        definition.append(check)
                        Point.add_extra_points()
                        if len(extra_list) % 2 == 0:
                            messages.info(request,"You earned 1 Point for 2 extra words")
                        messages.info(request, "Congrats, Extra Word Found!")
                        return redirect('level10')
                else:
                    messages.info(request, "Word doesn't exist, try again \n")
                    return redirect('level10')
            else:
                messages.info(request, "You have finished the level")
                messages.info(request, "-----------------------------------------------------------------------------"
                                       "-----------------------")
                messages.info(request, "Game Over")
                messages.info(request, "-----------------------------------------------------------------------------"
                                       "-----------------------")
                # context={'form':form, 'que':question}
                # return render(request, "term/level1.html", context)
                context = {'word':word_found, 'extra':extra_list, 'def':definition}
                return render(request,"term/done.html", context)
    else:
        form = levelone()
    context={'form':form, 'que':question, 'point':Point.get_points()}
    return render(request, "term/level10.html", context)
