import logging
import pathlib
import sys
import unittest

from DigitalLogicAnalysis.Inputs.max_terms import MaxTerms

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

myPath = pathlib.Path(__file__).parent.parent.parent.resolve()
sys.path.insert(0, myPath + '/../')


class InputModuleTestCase(unittest.TestCase):
    def setUp(self):
        self.here = str(pathlib.Path(__file__).parent.parent.parent.resolve())

    def test_int_array(self):
        a = MaxTerms(2)
        self.assertEqual(a.get_num_variables(), 2)
        self.assertEqual(a.get_terms(), None)

        a.set_terms([0, 2])
        self.assertEqual(a.get_terms(), [0, 2])

    def test_validation_str_array(self):
        a = MaxTerms(2)
        try:
            a.set_terms([0, '1'])
            self.assertEqual(False, True)
        except ValueError as e:
            self.assertEqual(str(e), "List can only contain Integers")

    def test_validation_max_value(self):
        a = MaxTerms(2)
        try:
            a.set_terms([0, 2, 6, 7])
            self.assertEqual(False, True)
        except ValueError as e:
            self.assertEqual(str(e), "All values in list must be lower than 2**num_variables and non negative")

    def test_validation_num_elements(self):
        a = MaxTerms(2)
        try:
            a.set_terms([0, 1, 2, 1, 2, 2, 2])
            self.assertEqual(a.get_terms(), [0, 1, 2])
        except ValueError as e:
            self.assertEqual(False, True)


if __name__ == '__main__':
    unittest.main()
