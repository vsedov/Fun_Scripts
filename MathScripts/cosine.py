#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: cosine
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


import numpy as np
import pyinspect as pi


class Cosine:
    def __init__(self, vector: np.ndarray, vector_2: np.ndarray):
        self.vectors = [vector, vector_2]
        print(self.cosine())
        
    def legnth_mult(self) -> int:
        norm_1 = round(np.linalg.norm(self.vectors[0]), 5)
        norm_2 = round(np.linalg.norm(self.vectors[1]), 5)
        return norm_1 * norm_2

    def dot_vector(self) -> int:
        return round(np.dot(self.vectors[0].T, self.vectors[1])[0][0], 5)

    def cosine(self) -> np.float128:
        """
        cosine conversion

        Converts a vector or the difference between the two vectors
        and find the angle between them

        Returns
        -------
        int:
            returns single number that is in degrees
        """
        if self.legnth_mult() == 0:
            return round((np.arccos(self.dot_vector()) * 180) / np.pi, 5)
        else:
            return round(
                (np.arccos(self.dot_vector() / self.legnth_mult()) * 180) / np.pi, 5
            )


def main() -> None:

    x, y = np.array([[1], [np.sqrt(3)]]), np.array([[-1], [np.sqrt(3)]])

    Cosine(x, y)


if __name__ == "__main__":
    pi.install_traceback()
    main()
