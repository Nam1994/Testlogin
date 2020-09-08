import os
import sys

sys.path.append(".")
from Utils.HTMLTestRunner import *
from TestCases.test_case_01 import SauDeMo

# get the directory path to output report file
dir = os.getcwd()

# get all tests from Login class
login1 = unittest.TestLoader().loadTestsFromTestCase(SauDeMo)

# create a test suite
test_suite = unittest.TestSuite([login1])

# open the report file
outfile = open(dir + "/SeleniumPythonTestSummary.html", "w", encoding='utf-8')

# configure HTMLTestRunner options
runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Acceptance Tests')

# run the suite using HTMLTestRunner
runner.run(test_suite)
outfile.close()
