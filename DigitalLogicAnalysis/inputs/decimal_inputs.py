#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from abc import ABC

# set the logger
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def check_if_all_entries_int(List: list):
    return all(isinstance(item, int) for item in List)


class DecimalInputs(ABC):

    def __init__(self, typeOfInput: str, num_variables: int):
        self.__typeOfInput = typeOfInput
        self.num_variables = num_variables
        self.terms = None

    def __terms_list_validation(self, decimal_positions):

        if not isinstance(decimal_positions, list):
            raise ValueError("List can only contain Integers")

        decimal_positions = list(set(decimal_positions))
        if not check_if_all_entries_int(decimal_positions):
            raise ValueError("List can only contain Integers")

        if len(decimal_positions) > pow(2, self.num_variables):
            raise ValueError("num variables and Max terms dont match")

        if max(decimal_positions) >= pow(2, self.num_variables) or min(decimal_positions) < 0:
            raise ValueError("All values in list must be lower than 2**num_variables and non negative")

        return True

    def set_terms(self, decimal_positions: list):
        if self.__terms_list_validation(decimal_positions):
            decimal_positions = list(set(decimal_positions))
            self.terms = decimal_positions

    def get_terms(self):
        return self.terms

    def get_num_variables(self):
        return self.num_variables

    def __repr__(self):
        return (f'{self.__typeOfInput} \n'
                f'Num of Variables:-{self.num_variables} \n'
                f'Terms:- {self.terms}\n')
