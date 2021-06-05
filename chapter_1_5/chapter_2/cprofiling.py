#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: cprofiling
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import cProfile

import pyinspect as pi

import palingrams


def main() -> None:
    cProfile.run("palingrams.find_palingrams()")


def container() -> None:
    print(palingrams.find_palingrams())


if __name__ == "__main__":
    pi.install_traceback()
    main()
