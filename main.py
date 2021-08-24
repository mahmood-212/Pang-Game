from turtle import Turtle, Screen
from scoreboard import Score
from paddle import Paddle
from ball import Ball
import time
speed_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
POSITION = "center"
FONT_SIZE = ("Courier", 80, "normal")
screen = Screen()
computer_control = Paddle((350, 0))
user_control = Paddle((-350, 0))
football = Ball()
r_score = Score((70, 200))
l_score = Score((-70, 200))
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


screen.listen()

screen.onkeypress(key="Up", fun=computer_control.move_up)
screen.onkeypress(key="Down", fun=computer_control.move_down)

screen.onkeypress(key="w", fun=user_control.move_up)
screen.onkeypress(key="s", fun=user_control.move_down)

is_game_on = True
while is_game_on:
    time.sleep(football.speed_move)
    screen.update()
    football.move()

    # Detect collision with wall
    if football.ycor() > 280 or football.ycor() < -280:
        football.bounce_y()

    # Detect collision with paddle
    if football.distance(computer_control) < 50 and football.xcor() > 320 or football.distance(user_control) < 50 and \
            football.xcor() < -320:
        football.bounce_x()
        # for i in speed_list:
        #     football.speed(speed_list[i])
        #     i += 1

    if football.xcor() > 400:
        l_score.score += 1
        l_score.clear()
        l_score.write(f"{l_score.score}", align=POSITION, font=FONT_SIZE)
        football.home()
        football.speed_move = 0.1
        football.bounce_x()

    elif football.xcor() < -400:

        r_score.score += 1
        r_score.clear()
        r_score.write(f"{r_score.score}", align=POSITION, font=FONT_SIZE)
        football.home()
        football.speed_move = 0.1
        football.bounce_x()




screen.exitonclick()