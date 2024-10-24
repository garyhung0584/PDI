def BMICalculation(weight,height):
    if weight < 3 or weight > 200:
        return 'ERROR INPUT'
    if height < 0.5 or height > 2.5:
        return 'ERROR INPUT'
    BMI = weight / (height ** 2)
