#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from .decimal_inputs import DecimalInputs

# set the logger
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class MaxTerms(DecimalInputs):
    def __init__(self, num_variables: int):
        super(MaxTerms, self).__init__("MaxTerms", num_variables)
