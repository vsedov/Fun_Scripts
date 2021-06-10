#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: test
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


import pyinspect as pi


def main() -> None:
    # I wanted to see if the file would load
    tst_file = "../chapter_2/2of4brif.txt"

    # Word: Stop can also become into Pots

    anagram_1 = "stop"
    anagram_2 = "pots"

    print(anagram_1, anagram_2)

    # we would first have to convert everything here into a list

    anagram_1 = list(anagram_1)
    anagram_2 = list(anagram_2)

    # if we try to see if the words are equal , what we would get is the
    # following

    print(anagram_1 == anagram_2)
    # Here you see that they are the same though - what we have to do here is
    # make sure that we sort those values within the right order

    print(f"({anagram_1}, {anagram_2})", sorted(anagram_2) == sorted(anagram_2))


if __name__ == "__main__":
    pi.install_traceback()
    main()
