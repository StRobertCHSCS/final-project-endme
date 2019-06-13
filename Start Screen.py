import turtle
Space = turtle.Screen()
Space.bgcolor("Black")
Space.title("Start")

Border = turtle.Turtle()
Border.speed(0)
Border.color("Purple")
Border.penup()
Border.setposition(-300,-300)
Border.pensize(5)
Border.pendown()
for side in range(4):
    Border.fd(600)
    Border.lt(90)
Border.hideturtle()

button = turtle.Turtle()
button.speed(0)
button.penup()
button.color("White")
button.setposition(0,-150)
button.write("PRESS ENTER TO START" ,font=("Courier", 30, "bold"), align='center')
button.hideturtle()

title = turtle.Turtle()
turtle.register_shape("Title.gif")
title.shape("Title.gif")
title.speed(0)
title.setposition(0,300)

turtle.done()