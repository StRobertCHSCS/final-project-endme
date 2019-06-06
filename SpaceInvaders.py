import random
import turtle

#Creating the screen
Space = turtle.Screen()
Space.bgcolor("Black")
Space.title("Space Invaders")

#Drawing a border
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

#Creating the ship
Ship = turtle.Turtle()
Ship.shape("triangle")
Ship.setposition(0, -250)
Ship.showturtle()
Ship.color("Light Blue")
Ship.lt(90)

#Moving the ship
Shipspeed = 10

def moveleft():
    Ship.penup()
    x = Ship.xcor()
    x -= Shipspeed
    Ship.setx(x)
    if x < - 250:
        x = - 250
        Ship.setx(x)

def moveright():
    Ship.penup()
    x = Ship.xcor()
    x += Shipspeed
    Ship.setx(x)
    if x > 250:
        x = 250
        Ship.setx(x)


#Making a bullet
Bullet = turtle.Turtle()
Bullet.shape("circle")
Bullet.color("white")
Bullet.shapesize(.25)
Bullet.penup()
Bullet.speed(0)
Bullet.hideturtle()

Bulletspeed = 25

#Creating bullet states ready to shoot and shooting
Bulletstate = "ready"

def shootbullet():
    global Bulletstate
    if Bulletstate == "ready":
        Bulletstate = "fire"
        X = Ship.xcor()
        Y = Ship.ycor() + 10
        Bullet.setposition(X,Y)
        Bullet.showturtle()




#Making the alien
alien = turtle.Turtle()
alien.shape("square")
alien.penup()
alien.speed(0)
alien.setposition(-250, 250)
alien.color("green")

alienspeed = 2

#Connecting keys to functions
turtle.listen()
turtle.onkeypress(moveleft, "Left")
turtle.onkeypress(moveright, "Right")
turtle.onkey(shootbullet, "space")

#Main loops
condition = "true"
while True:
    #Make alien move
    x = alien.xcor()
    x += alienspeed
    alien.setx(x)
    #Making the alien zig zag
    if alien.xcor() > 250:
        alienspeed *= -1
        y = alien.ycor()
        y -= 50
        alien.sety(y)

    if alien.xcor() < - 250:
        alienspeed *= -1
        y = alien.ycor()
        y -= 50
        alien.sety(y)
    #Shooting the bullet
    if Bulletstate == "fire":
        y = Bullet.ycor()
        y += Bulletspeed
        Bullet.sety(y)
    if Bullet.ycor() > 280:
        Bullet.hideturtle()
        Bulletstate = "ready"

turtle.done()