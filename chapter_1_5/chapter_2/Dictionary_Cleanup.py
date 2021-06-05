#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: Dictionary_Cleanup
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import string

import pyinspect as pi


def alphabet() -> str:
    """Alphabetic string"""
    return string.ascii_lowercase.translate({ord("a"): None, ord("i"): None})


# Method 1 - requires 1 function - this method, due to lambda will take more
# time  not good
def dictionary_cleanup(word_list: list) -> list[str]:
    return list(filter(lambda word: word not in alphabet(), word_list))


# Method 2 requires 2 function
def alpha_filter(pointer: str) -> bool:
    """Check if singular string is within an alhpabet set"""
    return pointer not in alphabet()


def dictionary_clean(word_list: str) -> list[str]:
    return list(filter(alpha_filter, word_list))


if __name__ == "__main__":
    pi.install_traceback()
