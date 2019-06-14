import random
import turtle
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

#Creating a score
score = 0
points = turtle.Turtle()
points.speed(0)
points.color("white")
points.penup()
points.setposition(-310,310)
style = "Score: %s" %score
points.clear()
points.write(style, False, align="left", font=("Courier", 16, "bold"))
points.hideturtle()

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

Bulletspeed = 40

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

#Randomizing alien spawning
alien1 = turtle.Turtle()
alien1.hideturtle()
alien1.shape("alien.gif")
alien1.penup()
alien1.speed(0)
alien1.setposition(-225,250)
alien1.color("green")
alien1.showturtle()

alien2 = turtle.Turtle()
alien2.hideturtle()
alien2.shape("alien.gif")
alien2.penup()
alien2.speed(0)
alien2.setposition(-150,250)
alien2.color("green")
alien2.showturtle()

alien3 = turtle.Turtle()
alien3.hideturtle()
alien3.shape("alien.gif")
alien3.penup()
alien3.speed(0)
alien3.setposition(-75,250)
alien3.color("green")
alien3.showturtle()

alien4 = turtle.Turtle()
alien4.hideturtle()
alien4.shape("alien.gif")
alien4.penup()
alien4.speed(0)
alien4.setposition(0,250)
alien4.color("green")
alien4.showturtle()


alien5 = turtle.Turtle()
alien5.hideturtle()
alien5.shape("alien.gif")
alien5.penup()
alien5.speed(0)
alien5.setposition(75,250)
alien5.color("green")
alien5.showturtle()

alien6 = turtle.Turtle()
alien6.hideturtle()
alien6.shape("alien.gif")
alien6.penup()
alien6.speed(0)
alien6.setposition(150,250)
alien6.color("green")
alien6.showturtle()

alien7 = turtle.Turtle()
alien7.hideturtle()
alien7.shape("alien.gif")
alien7.penup()
alien7.speed(0)
alien7.setposition(225,250)
alien7.color("green")
alien7.showturtle()

alien8 = turtle.Turtle()
alien8.hideturtle()
alien8.shape("alien.gif")
alien8.penup()
alien8.speed(0)
alien8.setposition(100,250)
alien8.color("green")
alien8.showturtle()

alienspeed1 = 8
alienspeed2 = 8
alienspeed3 = 8
alienspeed4 = 8
alienspeed5 = 8
alienspeed6 = 8
alienspeed7 = 8
alienspeed8 = 8


#Collision with bullet and alien
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
while True:
  #Make alien1 move
    x = alien1.xcor()
    x += alienspeed1
    alien1.setx(x)
        #Making alien1 zig zag
    if alien1.xcor() > 250:
        alienspeed1 *= -1
        y = alien1.ycor()
        y -= 50
        alien1.sety(y)

    if alien1.xcor() < - 250:
        alienspeed1 *= -1
        y = alien1.ycor()
        y -= 50
        alien1.sety(y)
    #Makiing alien2 move
    x = alien2.xcor()
    x += alienspeed2
    alien2.setx(x)
    # Making alien2 zig zag
    if alien2.xcor() > 250:
        alienspeed2 *= -1
        y = alien2.ycor()
        y -= 50
        alien2.sety(y)

    if alien2.xcor() < - 250:
        alienspeed2 *= -1
        y = alien2.ycor()
        y -= 50
        alien2.sety(y)
    #Making alien3 move
    x = alien3.xcor()
    x += alienspeed3
    alien3.setx(x)
    # Making alien3 zig zag
    if alien3.xcor() > 250:
        alienspeed3 *= -1
        y = alien3.ycor()
        y -= 50
        alien3.sety(y)

    if alien3.xcor() < - 250:
        alienspeed3 *= -1
        y = alien3.ycor()
        y -= 50
        alien3.sety(y)
    #Making alien4 move
    x = alien4.xcor()
    x += alienspeed4
    alien4.setx(x)
    # Making alien4 zig zag
    if alien4.xcor() > 250:
        alienspeed4 *= -1
        y = alien4.ycor()
        y -= 50
        alien4.sety(y)

    if alien4.xcor() < - 250:
        alienspeed4 *= -1
        y = alien4.ycor()
        y -= 50
        alien4.sety(y)
    #Making alien5 move
    x = alien5.xcor()
    x += alienspeed5
    alien5.setx(x)
    # Making alien5 zig zag
    if alien5.xcor() > 250:
        alienspeed5 *= -1
        y = alien5.ycor()
        y -= 50
        alien5.sety(y)

    if alien5.xcor() < - 250:
        alienspeed5 *= -1
        y = alien5.ycor()
        y -= 50
        alien5.sety(y)
    #Making alien6 move
    x = alien6.xcor()
    x += alienspeed6
    alien6.setx(x)
    # Making alien6 zig zag
    if alien6.xcor() > 250:
        alienspeed6 *= -1
        y = alien6.ycor()
        y -= 50
        alien6.sety(y)

    if alien6.xcor() < - 250:
        alienspeed6 *= -1
        y = alien6.ycor()
        y -= 50
        alien6.sety(y)

    # Make alien7 move
    x = alien7.xcor()
    x += alienspeed7
    alien7.setx(x)
    # Making alien1 zig zag
    if alien7.xcor() > 250:
        alienspeed7 *= -1
        y = alien7.ycor()
        y -= 50
        alien7.sety(y)

    if alien7.xcor() < - 250:
        alienspeed7 *= -1
        y = alien7.ycor()
        y -= 50
        alien7.sety(y)

    # Make alien8 move
    x = alien8.xcor()
    x += alienspeed8
    alien8.setx(x)
    # Making alien8 zig zag
    if alien8.xcor() > 250:
        alienspeed8 *= -1
        y = alien8.ycor()
        y -= 50
        alien8.sety(y)

    if alien8.xcor() < - 250:
        alienspeed8 *= -1
        y = alien8.ycor()
        y -= 50
        alien8.sety(y)
    #Shooting the bullet
    if Bulletstate == "fire":
        y = Bullet.ycor()
        y += Bulletspeed
        Bullet.sety(y)
    if Bullet.ycor() > 280:
        Bullet.hideturtle()
        Bulletstate = "ready"
    #collision with alien1
    if collision(Bullet, alien1)== True:
        Bullet.hideturtle()
        score += 10
        style = "Score: %s" % score
        points.clear()
        points.write(style, False, align="left", font=("Courier", 16, "bold"))
        Bulletstate = "ready"
        Bullet.setposition(0, -400)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        alien1.setposition(x, y)
    if collision(Ship, alien1):
        print ("GAME OVER")
    #Collision with alien2
    if collision(Bullet, alien2)== True:
        Bullet.hideturtle()
        score += 10
        style = "Score: %s" % score
        points.clear()
        points.write(style, False, align="left", font=("Courier", 16, "bold"))
        Bulletstate = "ready"
        Bullet.setposition(0, -400)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        alien2.setposition(x, y)
    if collision(Ship, alien2):
        print ("GAME OVER")
    #Collision with alien3
    if collision(Bullet, alien3)== True:
        Bullet.hideturtle()
        score += 10
        style = "Score: %s" % score
        points.clear()
        points.write(style, False, align="left", font=("Courier", 16, "bold"))
        Bulletstate = "ready"
        Bullet.setposition(0, -400)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        alien3.setposition(x, y)
    if collision(Ship, alien3):
        print ("GAME OVER")
    #Collision with alien4
    if collision(Bullet, alien4)== True:
        Bullet.hideturtle()
        score += 10
        style = "Score: %s" % score
        points.clear()
        points.write(style, False, align="left", font=("Courier", 16, "bold"))
        Bulletstate = "ready"
        Bullet.setposition(0, -400)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        alien4.setposition(x, y)
    if collision(Ship, alien4):
        print ("GAME OVER")
    #Collision with alien5
    if collision(Bullet, alien5)== True:
        Bullet.hideturtle()
        score += 10
        style = "Score: %s" % score
        points.clear()
        points.write(style, False, align="left", font=("Courier", 16, "bold"))
        Bulletstate = "ready"
        Bullet.setposition(0, -400)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        alien5.setposition(x, y)
    if collision(Ship, alien5):
        print ("GAME OVER")
    #Collision with alien6
    if collision(Bullet, alien6)== True:
        Bullet.hideturtle()
        score += 10
        style = "Score: %s" % score
        points.clear()
        points.write(style, False, align="left", font=("Courier", 16, "bold"))
        Bulletstate = "ready"
        Bullet.setposition(0, -400)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        alien6.setposition(x, y)
    if collision(Ship, alien6):
        print ("GAME OVER")
    #Collision with alien7
    if collision(Bullet, alien7)== True:
        Bullet.hideturtle()
        score += 10
        style = "Score: %s" % score
        points.clear()
        points.write(style, False, align="left", font=("Courier", 16, "bold"))
        Bulletstate = "ready"
        Bullet.setposition(0, -400)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        alien7.setposition(x, y)
    if collision(Ship, alien7):
        print ("GAME OVER")
    #Collision with alien8
    if collision(Bullet, alien8)== True:
        Bullet.hideturtle()
        score += 10
        style = "Score: %s" % score
        points.clear()
        points.write(style, False, align="left", font=("Courier", 16, "bold"))
        Bulletstate = "ready"
        Bullet.setposition(0, -400)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        alien8.setposition(x, y)
    if collision(Ship, alien8):
        print ("GAME OVER")

turtle.done()