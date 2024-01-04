
import time
from turtle import Screen
from padle import Padle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong game")

screen.tracer(0)

r_padle = Padle((350,0))
l_padle = Padle((-350,0))
ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_padle.up,"Up")
screen.onkey(l_padle.down,"Down")
screen.onkey(r_padle.up,"w")
screen.onkey(r_padle.down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
      # needs to bounse
      ball.bounce_y()
    # detect collision with right padle
    if ball.distance(r_padle) < 50 and ball.xcor() >320 or ball.distance(l_padle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # detect when r_padle miss
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
    # detect when l_padle miss
    if  ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()