try:
    name = input("Please enter your name: ")
    height_inch = float(input("Please enter your height in inches: "))
    height_m = float(height_inch / 39.37)
    weight_lb = float(input("Please enter your weight in pounds: "))
    weight_kg = float(weight_lb / 2.205)
except ValueError:
    print("Invalid Input")


def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("\n" + name + "'s BMI is: " + str(bmi) + ".\n")
    if bmi < 25:
        return name + " is not overweight."
    else:
        return name + " is overweight."


result = bmi_calculator(name, height_m, weight_kg)
print(result)
