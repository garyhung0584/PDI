import unittest
import myBMI


class TestBMI(unittest.TestCase):
    def test_computeBMIOK(self):
        self.assertEqual(myBMI.BMICalculation(201,1.8),'ERROR INPUT')
        self.assertEqual(myBMI.BMICalculation(52,0.05),'ERROR INPUT')
        self.assertEqual(myBMI.BMICalculation(2, 1.55),'ERROR INPUT')
        self.assertEqual(myBMI.BMICalculation(52,3),'ERROR INPUT')
        self.assertEqual(myBMI.BMICalculation(65, 1.8), '20.1')
