#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: myver_anagrams
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


import pyinspect as pi
from chapter_2.Dictionary_Cleanup import dictionary_clean
from chapter_2.load_dictionary import load_file

"""
    Different ways of doing this , i will go with list comp  as it is indeed faster and nicer to look at
"""


def list_filter(anagram_word: str) -> list[str]:
    anagram_word = sorted(anagram_word.lower())
    word_list = dictionary_clean(load_file("../chapter_2/2of4brif.txt"))
    return list(filter(lambda x: sorted(x) == anagram_word, word_list))


def find_anagram(anagram: str = None) -> list[str]:
    if anagram is None:
        anagram = str(input("Please enter a word to find an anagram"))

    s_anagram = sorted(anagram.lower())

    word_list = dictionary_clean(load_file("../chapter_2/2of4brif.txt"))

    return [word for word in word_list if sorted(word) == s_anagram and word != anagram]


def main() -> None:
    print(find_anagram("fortes"))


if __name__ == "__main__":
    pi.install_traceback()
    main()
