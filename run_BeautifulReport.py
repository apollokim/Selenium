import unittest
from BeautifulReport import BeautifulReport
import time

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    file_name = now + '测试报告.html'
    test_suite = unittest.defaultTestLoader.discover('./', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename=file_name, description='测试deafult报告', report_dir='report', theme='theme_memories')
