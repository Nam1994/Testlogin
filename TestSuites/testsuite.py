import sys

sys.path.append(".")
import unittest
from TestCases.test_case_01 import SauDeMo
from TestCases.test_product_checkout import SauDeMo


# get all tests from Login class
login = unittest.TestLoader().loadTestsFromTestCase(SauDeMo)
product_1 = unittest.TestLoader().loadTestsFromTestCase(SauDeMo)



# create a test suite
test_suite = unittest.TestSuite([login, product_1])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)
