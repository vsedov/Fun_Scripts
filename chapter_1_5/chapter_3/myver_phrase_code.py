#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: myver_phrase_code
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


from typing import Counter

import pyinspect as pi
from chapter_2.Dictionary_Cleanup import dictionary_clean
from chapter_2.load_dictionary import load_file


class Anagram:
    def __init__(self, name: str):
        self.main_phrase = ""
        self.name_letter_map = Counter(name)
        self.word_list = dictionary_clean(load_file("../chapter_2/2of4brif.txt"))
        print("Original name : ", name)
        print("----------------------------------------------------------------\n")

    def find_anagram(self) -> None:
        main_list = []
        for word in self.word_list:
            word_letter_count = Counter(word.lower())
            test = ""
            x = [
                word_letter_count[letter] <= self.name_letter_map[letter]
                for letter in word
            ]
            if all(x):
                main_list.append(word)

        print(*main_list, sep="\n")

        if len(main_list) == 0:
            print(
                "there are no possible words that can be made with remaining words : "
            )
            print(*self.name_letter_map)
            self.information_process()

        self.user_name_choice = str(
            input("Please enter a word that you would like to use for your phrase: ")
        )
        self.user_choice(main_list)

    def information_process(self) -> None:
        if len(self.name_letter_map) != 0:
            print("----------------------------------------------------------------")
            print("Remaining words were : ", self.name_letter_map)
        print("----------------------------------------------------------------")
        print("your anagram is , ", self.main_phrase)
        print("----------------------------------------------------------------")
        exit()

    def user_choice(self, listowords: list) -> None:
        if self.user_name_choice not in listowords:
            print("This name is not in the list, please try again ")
            self.find_anagram()
        else:

            self.main_phrase += f"{self.user_name_choice} "

            print("your current phrase is the following ", self.main_phrase)
            option = int(
                input(
                    "Would you like to continue? Enter 1 for yes to get another anagram or enter 0 to leave and exit the program "
                )
            )
            if option == 1:
                self.name_letter_map -= Counter(self.user_name_choice)
                print(self.name_letter_map)
                self.find_anagram()
            else:
                self.information_process()

    def start(self) -> None:
        self.find_anagram()


def main() -> None:
    user_input = str(input("Please enter your name : "))
    name = "".join(user_input.lower().split()).replace("-", "")

    Anagram(name).start()


if __name__ == "__main__":
    pi.install_traceback()
    main()
