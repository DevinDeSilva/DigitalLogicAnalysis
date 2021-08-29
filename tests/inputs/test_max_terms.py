import pathlib
import unittest

from DigitalLogicAnalysis.inputs.max_terms import MaxTerms


class InputModuleTestCase(unittest.TestCase):
    def setUp(self):
        self.here = str(pathlib.Path(__file__).parent.parent.parent.resolve())

    def test_int_array(self):
        a = MaxTerms(2)
        self.assertEqual(a.get_num_variables(), 2)
        self.assertEqual(a.get_terms(), None)

        a.set_terms([0, 2])
        self.assertEqual(a.get_terms(), [0, 2])  # add assertion here


if __name__ == '__main__':
    unittest.main()

