# FitnessFan App
# observe their BMI
# observe their BMR(Basel Metabolic Rate)
# observe daily calorie consumption expectation based on target weight goal

def bmi_calculator():
    global user_height
    global user_weight
    global bmi
    global A

    # Get user input for height, weight, and age
    user_height = float(input("What is your height(m): "))
    user_weight = float(input("What is your weight(kg): "))
    A = int(input('Enter your age: '))

    # Calculate BMI
    bmi = (user_weight) / (user_height ** 2)
    bmi = round(bmi, 3)

    # Print BMI
    print(f'Your BMI is: {bmi} kg/m^2')

def bmi_rating():
    if bmi < 18.5:
        print('You are Underweight')
    elif bmi < 24.9:
        print('You are on a Normal Weight')
    elif bmi >= 25 and bmi < 30:
        print('You are Overweight')
    else:
        print('You are Obese')

# Calories burned while at rest
def bmr():
    global BMR_M
    global BMR_W
    global gender

    gender = input('Are you F or M: ').upper()
    BMR_M = (10 * user_weight) + (6.25 * (user_height * 100)) - (5 * A) + 5
    BMR_W = (10 * user_weight) + (6.25 * (user_height * 100)) - (5 * A) - 161

    if gender == 'M':
        print('You will burn {} calories when resting'.format(BMR_M))
    elif gender == 'F':
        print('You will burn {} calories when resting'.format(BMR_W))

# Harris Benedict equation, the amount of calories burned in a day
def hb():
    user_activity = input('How often do you exercise (Little L, Light Exercise LE, Moderate M, Hard H, Extra Active EA): ')
    user_activity = user_activity.upper()

    if gender == 'M':
        if user_activity == 'L':
            calories_burned = BMR_M * 1.2
        elif user_activity == 'LE':
            calories_burned = BMR_M * 1.375
        elif user_activity == 'M':
            calories_burned = BMR_M * 1.55
        elif user_activity == 'H':
            calories_burned = BMR_M * 1.725
        elif user_activity == 'EA':
            calories_burned = BMR_M * 1.9
    elif gender == 'F':
        if user_activity == 'L':
            calories_burned = BMR_W * 1.2
        elif user_activity == 'LE':
            calories_burned = BMR_W * 1.375
        elif user_activity == 'M':
            calories_burned = BMR_W * 1.55
        elif user_activity == 'H':
            calories_burned = BMR_W * 1.725
        elif user_activity == 'EA':
            calories_burned = BMR_W * 1.9

    print('You will burn {} calories in a day with your activity level'.format(calories_burned))

bmi_calculator()
bmi_rating()
bmr()
hb()





