# import turtle
# t = turtle.Turtle()

# turtle.title("Flag of Vietnam")

# turtle.bgcolor("#DA251D")
# t.pencolor("#FFCD00")
# t.fillcolor("#FFCD00")

# t.penup()
# t.goto(-130, 50)
# t.pendown()

# t.begin_fill()

# for i in range(5):
#     t.fd(100)
#     t.lt(72)
#     t.fd(100)
#     t.rt(144)

# t.end_fill()

# t.hideturtle()

# turtle.mainloop()

#L I S T O F B R E H A N D L M A O

counter = 1

favfood = ["Pizza", "BBQ", "Steak", "Pho", "Instant Noodles"]

for i in range(len(favfood) - 1, -1, -1):
    print(str(counter) + ". " + favfood[i])
    counter = counter + 1