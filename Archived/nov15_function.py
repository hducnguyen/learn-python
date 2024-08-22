# games = ["PUBG", "AOV", "CSGO"]

# for i in range(len(games)):
#     print(str(i+1) + ". " + games[i])

# print()

# print("I like " + games[0] + " the most.")
# print("I only play " + games[1] + " with my friend. ")
# print("I don't really like " + games[2] + " too much. ")

# Function: block of code, reusable, can have input/output, must always have "()"

# def sayhi(): #define a function
#     print("Hi, nice to meet you")

# sayhi() #for activate the function

# def sayhitosomeone(name): #inside () are arguments/parameters/inputs
#     print("Hi " + name + ", nice to meet you!")

# r = input("What is the radius of the circle: ")

# def circlearea(r):
#     Area = float(r) ** 2 * 3.14
#     print("Area: " + str(Area))

# circlearea(r)

# HW: function for A of rectangle and triangle

#Rectangle Area

# l = float(input("Enter the length of the rectangle: "))
# w = float(input("Enter the width of the rectangle: "))


# def rectangle_area(l, w):
#     area = l * w
#     print("Area: " + str(area))

# rectangle_area(l, w)

# Triangle Area

h = float(input("Enter the height of the triangle: "))
b = float(input("Enter the base of the triangle: "))


def triangle_area(b, h):
    areaof_triangle = b * h / 2
    print("Area: " + str(areaof_triangle))

triangle_area(b, h)