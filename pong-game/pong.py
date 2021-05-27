import turtle
import winsound

wnd = turtle.Screen()
wnd.title("PONG by @zahrashahid8")
wnd.bgcolor("black")
wnd.setup(width=800,height=600)
wnd.tracer(0)

#Paddle A
p_a = turtle.Turtle()
p_a.speed(0)
p_a.shape("square")
p_a.color("white")
p_a.shapesize(stretch_wid=5,stretch_len=1)
p_a.penup()
p_a.goto(-350,0)

#Paddle B
p_b = turtle.Turtle()
p_b.speed(0)
p_b.shape("square")
p_b.color("white")
p_b.shapesize(stretch_wid=5,stretch_len=1)
p_b.penup()
p_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dy=-2
ball.dx=-2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PLAYER A: 0 | PLAYER B: 0", align="center", font=("Courier", 24, "normal"))

#Score
score_a =0
score_b =0

#moving functions
def p_a_up():
    y=p_a.ycor()
    y+=20
    p_a.sety(y)

def p_a_down():
    y=p_a.ycor()
    y-=20
    p_a.sety(y)


def p_b_up():
    y=p_b.ycor()
    y+=20
    p_b.sety(y)

def p_b_down():
    y=p_b.ycor()
    y-=20
    p_b.sety(y)


#keyboard binding
wnd.listen()
wnd.onkeypress(p_a_up,"w")
wnd.onkeypress(p_a_down,"s")
wnd.onkeypress(p_b_up,"Up")
wnd.onkeypress(p_b_down,"Down")


#Main game loop
while True:
    wnd.update()

    #Move the Ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("ball-bounce.mp3",winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("ball-bounce.mp3", winsound.SND_ASYNC)


    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("PLAYER A: {} | PLAYER B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score_b+=1
        pen.clear()
        pen.write("PLAYER A: {} | PLAYER B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    
    #Paddle and Ball Collisions
    if (ball.xcor()>340 and ball.xcor()<350 ) and (ball.ycor()< p_b.ycor()+40 and ball.ycor()> p_b.ycor()-40):
       ball.setx(340)
       ball.dx *= -1

    if (ball.xcor()<-340 and ball.xcor()>-350 ) and (ball.ycor()< p_a.ycor()+40 and ball.ycor()> p_a.ycor()-40):
       ball.setx(-340)
       ball.dx *= -1