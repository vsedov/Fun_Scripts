#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: Linear_equations
import ast

import numpy as np
from pprintpp import pprint as pp


class LinearEquations:
    def __init__(self, ath: np.array, bth: list[int]):

        self.A_matrix = ath
        self.B_matrix = bth
        """Pick method to solve x"""
        self.x = self.__option()

    def __option(self):
        try:
            x = int(
                input(
                    "Enter what method you would like :\n\n 1: Least Square Method \n\n 2: normal Linalg_solve"
                )
            )
            if x == 1:
                return self._least_squares_method()

            elif x == 2:
                return self._linalg_solve()
        except Exception as e:
            raise e

    def _linalg_solve(self) -> np.ndarray:
        """
        Linear alg solve

        Internal method for numpy Only works for 2x + y
        equations in which you have a quadtratic

        Returns
        -------
        np.ndarray:
            return x , y
        """
        return np.linalg.solve(self.A_matrix, self.B_matrix)

    def _least_squares_method(self) -> np.ndarray:
        """
        Least_Square_Method

        Ax=b→ X_ls = (Aᵀ∙A)⁻¹∙Aᵀ*b

        Returns
        -------
        np.ndarray:
            All xth unknown value using method defined in doc
        """
        return (
            np.linalg.inv(self.A_matrix.T * np.mat(self.A_matrix))
            * self.A_matrix.T
            * self.B_matrix
        )

    def __repr__(self):
        if self.x is not None:
            print("Following Ax=b\n")
            print("Shape of xth is :", self.x.shape, sep="\n")
            for ammount, variable in enumerate(self.x):
                print(f"{ammount} => {variable}")

            print("\n")
            return f"Ath:{self.A_matrix} times \n\n xth: {self.x} gives \n\n bth: {self.B_matrix}"

        return f"Ath:{self.A_matrix} * \n\nxth{self.B_matrix}"


def enter_matrix() -> np.ndarray:
    """
    enter_matrix -

    Convert String into a np.matrix using the ast package

    Returns
    -------
    np.ndarray:
        numpy array format matrix without any strings
    """
    return np.array(ast.literal_eval(str(input("Enter a matrix"))))


def main() -> None:
    matrix_a = enter_matrix()

    print("\nEnter for Matrix B/Bth matix within the Ax = b\n")
    matrix_b = enter_matrix()

    pp(LinearEquations(ath=matrix_a, bth=matrix_b))


if __name__ == "__main__":
    main()
