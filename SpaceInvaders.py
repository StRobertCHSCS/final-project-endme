import random
import turtle
import os
import math

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

# ship picture
turtle.register_shape("Spaceship.gif")

#Creating the ship
Ship = turtle.Turtle()
Ship.penup()
Ship.speed(0)
Ship.shape("Spaceship.gif")
Ship.setposition(0, -250)
Ship.showturtle()
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



# Images of aliens

turtle.register_shape("alien.gif")

# randomizing alien spawning
number_of_aliens = 6

aliens = []

for i in range(number_of_aliens):
    aliens.append(turtle.Turtle())
#Making the alien

for alien in aliens:
    alien.shape("alien.gif")
    alien.penup()
    alien.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    alien.setposition(x, y)
    alien.color("green")

alienspeed = 2

# collision with bullet and alien
def collision(c1, c2):
    distance = math.sqrt(math.pow(c1.xcor() - c2.xcor(), 2) + math.pow(c1.ycor() - c2.ycor(), 2))
    if distance < 25:
        return True
    else:
        return False

#Connecting keys to functions
turtle.listen()
turtle.onkeypress(moveleft, "Left")
turtle.onkeypress(moveright, "Right")
turtle.onkey(shootbullet, "space")

#Main loops
condition = "true"
while True:
    for alien in aliens:
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
    #collision with alien
    if collision(Bullet, alien):
        Bullet.hideturtle()
        Bulletstate = "ready"
        Bullet.setposition(0, -400)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        alien.setposition(x, y)

turtle.done()