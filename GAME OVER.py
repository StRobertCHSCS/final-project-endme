import turtle

space = turtle.Screen()
space.bgcolor("black")

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

game = turtle.Turtle()
turtle.register_shape ("GAME OVER.gif")
game.shape("GAME OVER.gif")
game.setposition(0,0)

turtle.done()