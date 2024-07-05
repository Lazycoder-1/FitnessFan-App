# FitnessFan App
# observe their BMI
# observe their BMR(Basel Metabolic Rate)
# observe daily calorie consumption expectation based on target weight goal

def bmi_calculator():
    global user_height
    global user_weight
    global bmi
    global A
    global BMR_M

    # Get user input for height, weight, and age
    user_height = float(input("What is your height(m): "))
    user_weight = float(input("What is your weight(kg): "))
    A = int(input('Enter your age: '))

    # Calculate BMI
    bmi = (user_weight) / (user_height ** 2)
    bmi = round(bmi, 3)

    # Print BMI
    print(f'Your BMI is: {bmi}')

    # Mifflin Equation to calculate BMR for males and females
    # BMR_M = (10 * user_weight) + (6.25 * (user_height * 100)) - (5 * A) + 5
    # print(f'Your BMR (Mifflin Equation) is: {BMR_M}')


def bmi_rating():
    if bmi < 18.5:
        print('You are Underweight')
    elif bmi < 24.9:
        print('You are on a Normal Weight')
    elif bmi > 25:
        print('You are Overweight')
    else:
        print('You are Obese')

def bmr():
    gender = input('Are you a F or M : ')
    BMR_M = (10 * user_weight) + (6.25 * (user_height * 100)) - (5 * A) + 5
    #print(f'Your BMR (Mifflin Equation) is: {BMR_M}')
    if gender == 'M':
        print(BMR_M)
    else:
        print('Working on it ')

bmi_calculator()
bmi_rating()
bmr()




