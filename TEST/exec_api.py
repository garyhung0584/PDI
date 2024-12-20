import coverage
import unittest

cov = coverage.coverage(branch=True,source=['myBMI'])
cov.start()
suite = unittest.defaultTestLoader.discover(".","myBMItest.py")
unittest.TextTestRunner().run(suite)
cov.stop()
cov.save()
cov.report()
cov.html_report(directory='cov')