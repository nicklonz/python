import turtle

# Set up the screen
win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

# Function to move the left paddle up
def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:
        y += 20
        left_paddle.sety(y)

# Function to move the left paddle down
def left_paddle_down():
    y = left_paddle.ycor()
    if y > -240:
        y -= 20
        left_paddle.sety(y)

# Function to move the right paddle up
def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        y += 20
        right_paddle.sety(y)

# Function to move the right paddle down
def right_paddle_down():
    y = right_paddle.ycor()
    if y > -240:
        y -= 20
        right_paddle.sety(y)

# Keyboard bindings
win.listen()
win.onkeypress(left_paddle_up, "w")
win.onkeypress(left_paddle_down, "s")
win.onkeypress(right_paddle_up, "Up")
win.onkeypress(right_paddle_down, "Down")

while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle collision
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50):
        ball.color("blue")
        ball.dx *= -1

    elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50):
        ball.color("red")
        ball.dx *= -1
