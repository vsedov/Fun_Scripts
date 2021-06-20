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

    x = counter([i for i in anagram_1])


if __name__ == "__main__":

    pi.install_traceback()
    main()
