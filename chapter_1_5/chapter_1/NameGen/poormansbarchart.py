#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: poormansbarchart
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


import string
from collections import defaultdict
from typing import Counter

import pyinspect as pi
from pprintpp import pprint as pp


def bar_chart(sentence: str) -> dict:
    alphabet = string.ascii_lowercase
    filtered_letter = "".join(i for i in sentence if i in alphabet)
    sentence = sorted("".join(filtered_letter.lower().split()))
    word_amount = Counter(sentence)

    for key, value in word_amount.items():
        word_amount[key] = [key for _ in range(value)]

    return word_amount


# Solutions to there method ,
def better_method(sentence: str) -> dict:
    alphabet = string.ascii_lowercase
    mapped = defaultdict(list)

    for characters in sentence:
        character = characters.lower()
        if character in alphabet:
            mapped[characters].append(characters)

    return mapped


def main() -> None:
    # sentence = str(input("Enter a sentence :"))
    sentence = "Like the castle in its corner in medeval game, io forsee terrible trouble and I stay here just the same."

    pp(better_method(sentence))
    print("my version")

    pp(bar_chart(sentence))


if __name__ == "__main__":
    pi.install_traceback()
    main()
