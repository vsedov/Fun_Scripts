#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: Counter_stuff
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import Counter

import pyinspect as pi
from icecream import ic


def method_1(main_name: str, name_letter_map: dict, word_list: list) -> None:

    for word in word_list:
        word_map = Counter(word)

        test_word = ""
        for letter in word_map:
            if word_map[letter] <= name_letter_map[letter]:
                test_word += letter
        if Counter(test_word) == word_map:
            ic(word)


def method_2(main_name: str, name_letter_map: dict, word_list: list) -> None:
    container = []
    for word in word_list:
        test = ""
        word_map = Counter(word)


def main() -> None:
    main_name = "forest"
    name_letter_map = Counter(main_name)
    print(len(name_letter_map))
    word_list = ["fost", "of", "for", "hambugger", "test"]

    print(name_letter_map - Counter("of"))
    # method_2(main_name, name_letter_map, word_list)


# What this script does is get the words within a list, using a counter , with
# teh iven words that you have already had, which is new and i had not known
# that i could do something like


if __name__ == "__main__":
    pi.install_traceback()
    main()
