from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=650,height=650)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
snake.createborder()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

gamenotover = True
while gamenotover:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:   #distance method comparison with snake,head segment wth food x.distance(y) distance between x and y
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or  snake.head.ycor() < -280 :
         gamenotover = False
         score.gameover()
    for part in snake.parts[1:]:
        if snake.head.distance(part) < 10:
            gamenotover = False
            score.gameover()
screen.exitonclick()