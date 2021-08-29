import logging

from . import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

__all__ = [
    'min_terms',
    'max_terms',
    'dont_care_terms'
]
