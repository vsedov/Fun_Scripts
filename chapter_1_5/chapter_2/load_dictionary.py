#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: load_dictionary
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import sys

import pyinspect as pi
from pprintpp import pprint as pp


def load_file(file: str) -> list:
    """Open a text file and turn contents into a list of lowercase strings"""
    try:
        with open(file, "r") as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            return [x.lower() for x in loaded_txt]

    except IOError as e:
        print(f"{e} error occoured on file {file}", file=sys.stderr)

    finally:
        in_file.close()


def main() -> None:
    # Example of loading file
    pp(load_file("6of12.txt"))


if __name__ == "__main__":
    pi.install_traceback()
    main()
