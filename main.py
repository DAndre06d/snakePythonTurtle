from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snek Game")
screen.tracer(0)

snek = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(key="Up", fun=snek.turn_up)
screen.onkey(key="Down", fun=snek.turn_down)
screen.onkey(key="Right", fun=snek.turn_right)
screen.onkey(key="Left", fun=snek.turn_left)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snek.move()
    if snek.head.distance(food) < 15:
        snek.extend()
        scoreboard.increase_score()
        food.refresh()
    if snek.head.xcor() > 280 or snek.head.xcor() < -280 or snek.head.ycor() > 280 or snek.head.ycor() < -280:
        scoreboard.reset()
        game_on = False
        scoreboard.game_over()
    for segment in snek.segment[1:]:
        if snek.head.distance(segment) < 10:
            scoreboard.reset()
            game_on = False
            scoreboard.game_over()


screen.exitonclick()


