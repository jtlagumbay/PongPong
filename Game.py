import turtle


win = turtle.Screen()
win.title("PongPong")
win.bgcolor("peach puff")
win.setup(width=600, height=600)
win.tracer(0)

#Score
scoreA = 0
scoreB = 0


#Paddle A
padA = turtle.Turtle()
padA.speed(0)
padA.shape("square")
padA.color("dark red")
padA.shapesize(stretch_len=5, stretch_wid=1)
padA.penup()
padA.goto(0, 270)


#Paddle B
padB = turtle.Turtle()
padB.speed(0)
padB.shape("square")
padB.color("crimson")
padB.shapesize(stretch_len=5, stretch_wid=1)
padB.penup()
padB.goto(0, -270)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("light salmon")
ball.penup()
ball.goto(0,0)
ball.dx = 0.15
ball.dy = 0.15

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("blanched almond")
pen.penup()
pen.hideturtle()
pen.goto(0,-2)
pen.write(f"Player A: {scoreA}\n\nPlayer B: {scoreB}", align="center", font=("bebas", 20, "normal"))

#Function
def padA_right():
    x = padA.xcor()
    if x != 270:
        x += 30
    padA.setx(x)

def padA_left():
    x = padA.xcor()
    if x != -270:
        x -= 30
    padA.setx(x)

def padB_right():
    x = padB.xcor()
    if x != 270:
        x += 30
    padB.setx(x)

def padB_left():
    x = padB.xcor()
    if x != -270:
        x -= 30
    padB.setx(x)

#Keyboard binding
win.listen()
win.onkeypress(padA_right, "d")
win.onkeypress(padA_left, "a")
win.onkeypress(padB_right, "Right")
win.onkeypress(padB_left, "Left")



#Main Game
while True:
    win.update()

    #Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Control
    if ball.xcor()>290:
        ball.setx(290)
        ball.dx *= -1


    if ball.xcor()<-290:
        ball.setx(-290)
        ball.dx *= -1


    if ball.ycor()>290:
        ball.goto(0,0)
        ball.dy *= -1


    if ball.ycor()<-290:
        ball.goto(0,0)
        ball.dy *= -1

    #Collisions
    if (ball.ycor()>260 and ball.ycor()<280) and (ball.xcor() < padA.xcor()+40 and ball.xcor()>padA.xcor()-40):
        ball.sety(260)
        ball.dy *=-1
        scoreA += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}\n\nPlayer B: {scoreB}", align="center", font=("bebas", 20, "normal"))

    if (ball.ycor()<-260 and ball.ycor()>-280) and (ball.xcor() < padB.xcor()+40 and ball.xcor()>padB.xcor()-40):
        ball.sety(-260)
        ball.dy *=-1
        scoreB += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}\n\nPlayer B: {scoreB}", align="center", font=("bebas", 20, "normal"))
