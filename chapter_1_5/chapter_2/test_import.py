#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: test_import
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import pyinspect as pi

from load_dictionary import load_file


def main() -> None:
    load_file("test")


if __name__ == "__main__":
    pi.install_traceback()
    main()
