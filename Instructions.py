import turtle
#Screen
Instruc = turtle.Screen()
Instruc.bgcolor("black")
Instruc.title("Instructions")

#Border
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

#Instructions
Play = turtle.Turtle()
Play.color("White")
Play.speed(0)
Play.penup()
Play.setposition(0,200)
Play.write('How To Play', font=("Courier", 40, "bold"), align='center')
Play.hideturtle()

turtle.done()


