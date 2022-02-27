from turtle import Screen
import time
from snake import Snake
from food import SnekFood
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snek!")
screen.tracer(0)
game_on = True

snek = Snake()
snek_food = SnekFood()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")


while game_on:
    screen.update()
    time.sleep(0.1)
    snek.move_snake()

#   collision detection with food
    if snek.head.distance(snek_food) < 15:
        snek_food.got_eaten()
        scoreboard.add_score()
        snek.extend()
        print("yum!")

#   Detect collision with wall
    if snek.head.xcor() > 390 or snek.head.xcor() < -390 or snek.head.ycor() > 390 or snek.head.ycor() < -390:
        game_on = False
        scoreboard.game_over()

#   Detect collision with tail
    for segment in snek.segments_list[1:]:
        if snek.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
