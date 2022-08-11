from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

paddle_right = Paddle(350, 0)
paddle_left = Paddle(-350, 0)
ball = Ball()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(paddle_right.up, "Up")
screen.onkeypress(paddle_right.down, "Down")
screen.onkeypress(paddle_left.up, "w")
screen.onkeypress(paddle_left.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_y()
    # detect collision with right paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.ball_speed *= 0.9
    # detect if ball passed the wall
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()
        ball.ball_speed = 0.1

    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()
        ball.ball_speed = 0.1

screen.exitonclick()