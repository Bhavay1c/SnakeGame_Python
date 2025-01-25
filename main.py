# Bhavay Garg
# This class is the main class which creates objects of other class and control the game by calling respective methods   

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreKeeper

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("WELCOME TO MY SCREEN GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreKeeper()
current_score = 0

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(snake.right, "Right")
# use pascal code first letter capital for arrow keys  up is Up
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #     to detect collision with food
    if snake.head.distance(food) < 15:
        # we used 15 as the size of food is 10 by 10 so if distance between both turtles is than 15 then they collided
        current_score += 1
        snake.extend()
        food.refresh()

    score.score_keeping(current_score)

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        print(f"You are out of the game final score is {current_score} ")
        score.game_over()


    # detect collision with tail we can check that by checking the distance between head and each segment
#     for segment in snake.segments:
#         if segment == snake.head:
#             pass
#         elif snake.head.distance(segment) < 10:
#             game_on = False
#             score.game_over()
 

#     above code can also be written as below using slicing  [start:end:gap]  

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()




screen.exitonclick()
