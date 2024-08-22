import random
# input [2]: weight, height
# output [1]: float of BMI
def calculateBMI(weight, height) -> float:
    BMI = weight / height**2
    print("Your BMI is " + str(BMI))
    return BMI

def getBMIcategory(BMI):
    if BMI < 18.5:
        print("You are under weight")
    elif BMI >= 18.5 and BMI < 24.9:
        print("You are normal")
    elif BMI >= 25 and BMI < 29.9:
        print("You are overweight")
    elif BMI >= 30 and BMI < 34.9:
        print("You are obesity class 1")
    elif BMI >= 35 and BMI < 39.9:
        print("You are obesity class 2")
    elif BMI > 40:
        print("You are extreme obesity")

def BMIapp():
    height = float(input("Enter your height in m "))
    weight = float(input("Enter your weight in kgs "))

    BMI = calculateBMI(weight, height)
    getBMIcategory(BMI)

BMIapp()

countries = [
    {
        'name': 'Vietnam',
        'capital': 'hanoi'
    },
    {
        'name': 'USA',
        'capital': 'Washington DC'
    },
    {
        'name': 'Canada',
        'capital': 'Ottawa'
    },
    {
        'name': 'Australia',
        'capital': 'Canberra'
    },
    {
        'name': 'Brazil',
        'capital': 'Brasília'
    },
    {
        'name': 'Japan',
        'capital': 'Tokyo'
    },
    {
        'name': 'Germany',
        'capital': 'Berlin'
    },
    {
        'name': 'Mexico',
        'capital': 'Mexico City'
    },

]
# countryNum = random 
# print(countryNum)