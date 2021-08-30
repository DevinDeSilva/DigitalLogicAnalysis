#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from .decimal_inputs import DecimalInputs

# set the logger
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class DontCareTerms(DecimalInputs):
    def __init__(self, num_variables: int):
        super(DontCareTerms, self).__init__("DontCareTerms", num_variables)
