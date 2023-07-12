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
from icecream import ic

import load_dictionary


def question(question: str) -> str:
    return pi.ask(question)


def find_palingrams() -> list:
    word_list = set(load_dictionary.load_file("2of4brif.txt"))
    print("working")

    # MAYBE: a set as it would sort it for you ?
    palingrams = []

    for word in word_list:
        end = len(word)
        if end > 1:
            reverse_word = word[::-1]
            for i in range(end):
                if (
                    word[i:] == reverse_word[: end - i]
                    and reverse_word[: end - i] in word_list
                ):
                    palingrams.append((word, reverse_word[: end - i]))

                if (
                    word[:i] == reverse_word[: end - i]
                    and reverse_word[: end - i] in word_list
                ):
                    palingrams.append(("reverse", word, reverse_word[: end - i]))

    return sorted(palingrams)


def understanding(word: str) -> None:

    reverse_word = word[::-1]

    end = len(word)
    print(reverse_word[:end])
    print(reverse_word)
    print(reverse_word[: end - 1])

    start = [
        (word[i:], reverse_word[: end - i], (word[i:] == reverse_word[: end - i]))
        for i in range(end)
    ]
    end = [
        (word[:i], reverse_word[: end - i], (word[:i] == reverse_word[: end - i]))
        for i in range(end)
    ]

    ic(start)
    print("\n")
    ic(end)


def main() -> None:
    # question("how to create palingrams?")
    print(*find_palingrams(), sep="\n")
    print("\n")

    understanding("cardamom")
    print("\n")
    understanding("redder")


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


i := range(len(word))
word[i:] =>
            x x x x
            o x x x
            o o x x
            o o o x
            o o o o

word[:i] =>
            o o o o
            x o o o
            x x o o
            x x x o
            x x x x


Why does the reverse work ?
    if rv_word[:end] => end = len(rev_word)

    Refer to this code sample
    rv_word[:end]
    rv_word
    rv_word[:end-1]
        redder
        redder
        redde

rv_word[:end-i] =>
            x x x x
            x x x o
            x x o o
            x o o o
            o o o o
"""
