from myBMI import BMICalculation
 
def printResult(weight, height):
    bmi = BMICalculation(weight, height)
    if bmi < 18.50:
        return 'Underweight'
    elif bmi < 24 and bmi >= 18.50:
        return 'Normal'
    elif bmi < 27 and bmi >= 24:
        return 'Overweight'
    else:
        return 'Obesity'