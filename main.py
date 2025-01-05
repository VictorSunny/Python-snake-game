import turtle as t
from scoreboard import Scoreboard
from snakemodule import Snakegame
from food import Food
import time
s = t.Screen()
s.setup(600, 600)
s.bgcolor("black")
s.tracer(0)
s.listen()

for j in range(6):
    f = Snakegame()
gameon = True
food = Food()
sb = Scoreboard()
head = f.snake[0]
while gameon:
    s.title(f"Snake Score  {sb.score}")
    head.movesnake()
    s.update()
    time.sleep(0.07)
    head.snake_controls()
    if head.distance(food) < 15:
        food.appear()
        f = Snakegame()
        sb.renew()
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        sb.fail()
        gameon = False
    for block in f.snake:
        if head.distance(block) <= 0 and head != block:
            sb.fail()
            gameon = False
s.exitonclick()
