import coverage
import unittest

cov = coverage.coverage(branch=True,source=['PrintResult'])
cov.start()
suite = unittest.defaultTestLoader.discover("./","PrintResulttest.py")
unittest.TextTestRunner().run(suite)
cov.stop()
cov.save()
cov.report()
cov.html_report(directory='cov')