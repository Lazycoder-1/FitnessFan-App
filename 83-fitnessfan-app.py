# FitnessFan App
# observe their BMI
# observe their BMR(Basel Metabolic Rate)
# observe daily calorie consumption expectation based on target weight goal

def bmi_calculator():
    global user_height
    global user_weight
    global bmi

    user_height = float(input("What is your height(m): "))
    user_weight = float(input("What is your weight(kg): "))

    bmi = (user_weight)/(user_height)**2
    bmi = round(bmi,3)
    print('Your BMI is {} kg/m^2'.format(bmi))

def bmi_rating():
    if bmi < 18.5:
        print('You are Underweight')
    elif bmi < 24.9:
        print('You are on a Normal Weight')
    elif bmi >= 25:
        print('You are Overweight')
    else:
        print('You are Obese')


bmi_calculator()
bmi_rating()




