#! python3

import turtle
import winsound

window = turtle.Screen()
window.title("Pong by @ChuckCoggins")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Left Paddle
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Right Paddle
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)


def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)


def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)


def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)


# Main Game Loop
def start_game():
    press_p.clear()
    start_text.clear()
    while True:
        window.update()
        # Score
        score_a = 0
        score_b = 0

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border Checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("bonk.wav", winsound.SND_ASYNC)

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("bonk.wav", winsound.SND_ASYNC)

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))

        # Paddle and Ball  Collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 51 and ball.ycor() > paddle_right.ycor() - 51):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("tink.wav", winsound.SND_ASYNC)

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 51 and ball.ycor() > paddle_left.ycor() - 51):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("tink.wav", winsound.SND_ASYNC)


# Keyboard Binding
window.listen()
window.onkeypress(paddle_left_up, "w")
window.onkeypress(paddle_left_down, "s")
window.onkeypress(paddle_right_up, "Up")
window.onkeypress(paddle_right_down, "Down")
window.onkeypress(start_game, "p")

# Start Game
press_p = turtle.Turtle()
press_p.speed(0)
press_p.color("white")
press_p.penup()
press_p.hideturtle()
press_p.goto(0, 20)  # Places text at the middle of the screen
press_p.write("To Begin Playing Press 'p':", align="center", font=("Courier", 30, "normal"))
winsound.PlaySound("theme.wav", winsound.SND_ASYNC)
start_text = turtle.Turtle()
start_text.speed(0)
start_text.color("blue")
start_text.penup()
start_text.hideturtle()
start_text.goto(0, -30)  # Places text in middle below previous text above
start_text.write("Player A: Paddle Up = 'w' Paddle Down = 's'\nPlayer B: Paddle Up = 'Up Key' Paddle Down = 'Down Key'", align="center", font=("Courier", 14, "normal"))
window.mainloop()
