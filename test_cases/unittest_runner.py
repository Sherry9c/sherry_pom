import unittest
from datetime import datetime, date
import time
from pathlib import Path
from HTMLTestReportCN import HTMLTestRunner

# test suite配置
# case_path = r'./test51_cases'
# suite = unittest.defaultTestLoader.discover(case_path)
from test_cases.test51_cases.test_case01 import TestCase01

# suite = unittest.TestSuite()
# suite.addTest(TestCase01('test_01_login'))

suite=unittest.TestLoader().loadTestsFromTestCase(TestCase01)

# HTMLTestRunner配置
verbosity = 1
title = 'UITest Report'
description = 'There is description.'
tester = 'sherry'

report_path = '../report'
report_file = f'{report_path}/{time.strftime("%Y-%m-%d-%H%M%S")}.html'
# report_file = f'{report_path}/{time.strftime("%Y-%m-%d-%H%S%M")}.txt'
if not Path(report_path).is_dir():
    Path(report_path).mkdir()

with open(report_file, 'wb') as f:
    runner = HTMLTestRunner(f, verbosity=verbosity, title=title, description=description)
    runner.run(suite)

# with open(report_file,'w',encoding='utf-8') as f:
#     runner=unittest.TextTestRunner(f)
#     runner.run(suite)

# if __name__ == '__main__':
#     unittest.main()