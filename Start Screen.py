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

turtle.done()