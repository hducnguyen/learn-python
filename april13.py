a = int(input(("Enter number a: ")))
b = int(input(("Enter number b: ")))
c = int(input(("Enter number c: ")))
x1 = 0
x2 = 0
equation = a*x**2 + b*x + c

def tinh(): 
    delta = (b**2) - (4*a*c)

    if delta > 0:
        x1 = (-b +  delta**1/2) / 2*a
        x2 = (-b -  delta**1/2) / 2*a
    elif delta == 0:
        x1 = x2 = (-b)/(2*a)
    else:
        x1 = x2 = "undefined"

tinh()  