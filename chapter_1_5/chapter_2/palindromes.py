#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: palindromes
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


import pyinspect as pi

import load_dictionary


# Might add this to be really quick depending on how i would code
def question(question: str) -> str:
    return pi.ask(question)


def basic_stuff() -> None:
    word = "nurses"
    print(word[:])
    print(word[::-1])
    # What we can do here then is do the following

    print("s", word[2::-1])

    word = "nun"
    if word != word[::-1]:
        print("this is not a palidron")
    else:
        print(f"{word} is a palidrome good job")


def palindromes() -> list:
    # We are calling the function that was made before
    word_list = load_dictionary.load_file("6of12.txt")

    # Prefer using list comp in this case
    palindrome_list = [
        word for word in word_list if word == word[::-1] and len(word) > 2
    ]

    print(f"ammount of palindroms in file : {len(palindrome_list)}")

    return palindrome_list


def main() -> None:
    print(*palindromes(), sep="\n")
    # Did not know of this little trick printing wise

    # print("\n")
    # pp(palindromes())


if __name__ == "__main__":
    pi.install_traceback()
    main()
