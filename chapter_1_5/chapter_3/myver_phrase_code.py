#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: myver_phrase_code
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


import pyinspect as pi
from chapter_2.load_dictionary import load_file

from myver_anagrams import find_anagram


# Not effective , do not approve of this function that has been made
def test_function(name: str) -> list[str]:

    container = []
    remaining = ""
    for i in range(len(name)):
        anagram = find_anagram(name[:i])
        if len(anagram) != 0:
            for i in anagram:
                container.append(i)
        else:
            remaining += name[i]

    print(container)
    print(remaining)

    # is that what we are supposed to be doing ? Interesting question i must say
    # - will ponder over this later
    print(find_anagram(remaining))


def phrase_code(name: str = None) -> None:
    word_list = load_file("../chapter_2/2of4brif.txt")
    if name is None:
        name = str(input("Please enter a name"))

    test_function(name)


def main() -> None:
    phrase_code("forster")


if __name__ == "__main__":
    pi.install_traceback()
    main()
