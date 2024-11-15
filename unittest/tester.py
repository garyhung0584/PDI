import coverage
import unittest

cov = coverage.Coverage(branch=True, source=['poker'])
cov.start()
suite = unittest.defaultTestLoader.discover("./unittest","pokertest.py")
unittest.TextTestRunner().run(suite)
cov.stop()
cov.save()
cov.report()
cov.html_report(directory='cov')