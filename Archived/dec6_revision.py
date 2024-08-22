currentweight = int(input("Enter your weight: "))
height = float(input("Enter your height in meters: "))

bmi = currentweight / height ** 2

print("Your BMI is: " + str(bmi))

healthybmi = 24.9

newweight = healthybmi * height ** 2

if bmi <= 18.5:
    print("You're underweight. Eat more stuff")
    print("Your target is to reduce your weight to " + str(newweight) + " kg")
elif bmi >= 18.5 and bmi < 24.9:
    print("You're normal weight, keep it up!")
elif bmi >= 25 and bmi < 29.9:
    print("You're overweight, try to lose some weight")
    print("Your target is to reduce your weight to " + str(newweight) + " kg")
elif bmi >= 30:
    print("You're VERY overweight, please focus more on your diet.")
    print("Your target is to reduce your weight to " + str(newweight) + " kg")
