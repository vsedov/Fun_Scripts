#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: myver_voldermort
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import pyinspect as pi
from chapter_2.load_dictionary import load_file

# Changing how things would sound


class AnagramFinder:
    def __init__(self, main_word: str):
        self.word_list = load_file("../chapter_2/2of4brif.txt")
        self.trigram_list = load_file("least-likely_trigrams.txt")
        self.main_word = "".join(main_word.lower().split()).replace("-", "")

        # Option for user input as well .
        self.complete_output()

    def list_filter(self) -> list[str]:
        # we want to make sure that the names would then have the same legnth
        new_list = [
            word.lower()
            for word in self.word_list
            if len(word) == (len(self.main_word))
        ]
        print(f"{len(new_list)} ")
        return new_list

    def word_filter(self) -> None:
        pass

    def trigram_filter(self) -> None:
        pass

    def constant_filter(self) -> None:
        pass

    def filter_digrams(self) -> None:
        pass

    def filter_options(self) -> None:
        pass

    def complete_output(self) -> None:

        pass


def main() -> None:
    AnagramFinder("tmvoordle")


if __name__ == "__main__":
    pi.install_traceback()
    main()
