import unittest
import PrintResult


class TestPrintResult(unittest.TestCase):
    def test_printResult(self):
        self.assertEqual(PrintResult.printResult(50,1.8),'Underweight') #15.4
        self.assertEqual(PrintResult.printResult(65, 1.8), 'Normal')    #20.1
        self.assertEqual(PrintResult.printResult(60,1.5),'Overweight')  #26.7
        self.assertEqual(PrintResult.printResult(80,1.5),'Obesity')     #35.6
