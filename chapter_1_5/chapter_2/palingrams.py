#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: palingrams
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import pyinspect as pi

import load_dictionary


def question(question: str) -> str:
    return pi.ask(question)


def find_palingrams() -> list:
    word_list = set(load_dictionary.load_file("2of4brif.txt"))
    print("working")

    # MAYBE: a set as it would sort it for you ?
    palingrams = []

    for word in word_list:
        reverse_word = word[::-1]
        end = len(word)
        if end > 1:
            for i in range(end):
                if (
                    word[i:] == reverse_word[: end - i]
                    and reverse_word[: end - i] in word_list
                ):
                    # breakpoint()

                    palingrams.append((word, reverse_word[: end - i]))

                if (
                    word[:i] == reverse_word[: end - i]
                    and reverse_word[: end - i] in word_list
                ):

                    # breakpoint()

                    palingrams.append((word, reverse_word[: end - i]))

    return sorted(palingrams)


def main() -> None:
    # question("how to create palingrams?")
    print(*find_palingrams(), sep="\n")


if __name__ == "__main__":
    pi.install_traceback()
    main()

"""
    Psuedo code : 

    1. load digital dictionary as a list of words
    2. start an empty list to hold these words
    3. for word in word list:
        get legnth of word
        if legnth >1 :
            loop through the letters in the word:
                if reversed word fragement at front of word is in the word list and letters after form a palindromic sequence:
                    append reversed word to palingram list

                if reversed word fragement at end of word is in word list and letters before form a palindromic sequence:
                    append reveresed word to palingram list
"""

"""
    1 we are looking if some word in the list[i:] == reverse[::(word_ammount)-i] 
"""
