from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

count = 0
x_pos = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Sapola")


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.11)
    snake.move()

    # detectCollisionMove
    if snake.head.distance(food) < 16:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # collision with wall
    if snake.head.xcor() > 282 or snake.head.xcor() < -282 or snake.head.ycor() > 282 or snake.head.ycor() < -282:
        game_on = False
        scoreboard.game_over()

    # collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
