from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# from levels import Levels

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.06)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    # Detect collision with tail

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    # def level1():
    #     wall1 = Levels()
    #     wall2 = Levels()
    #     wall1.goto(-200, 0)
    #     wall2.goto(200, 0)
    #
    #     if wall1.distance(snake.head) < 25 or wall2.distance(snake.head) < 25:
    #         scoreboard.game_over()
    #         global game_is_on
    #         game_is_on = False
    #
    #
    # def level2():
    #     wall1 = Levels()
    #     wall2 = Levels()
    #     wall1.goto(0, -200)
    #     wall2.goto(0, 200)
    #
    #     if wall1.distance(snake.head)<50 or wall2.distance(snake.head)<50:
    #         scoreboard.game_over()
    #         global game_is_on
    #         game_is_on = False
    #
    # if scoreboard.score > 1:
    #     level1()
    #
    # if scoreboard.score > 2:
    #     level2()






screen.exitonclick()
