from turtle import Turtle as t, Screen

class Snakegame(t):
    snake= []
    x = 0
    screen = Screen()
    screen.listen()
    def __init__(self):
        super().__init__()
        def create(self):
            self.penup()
            self.shape("square")
            self.color("white")
            self.goto(self.x, 0)
            return self
        block = create(self)
        self.snake.append(block)
        Snakegame.x -= 20



    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)
    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)
    def left(self):
        if self.snake[0].heading() != 0:
           self.snake[0].setheading(180)

    def movesnake(self):
        for k in range(len(self.snake) - 1, 0, -1):
            xc = self.snake[k - 1].xcor()
            lc = self.snake[k - 1].ycor()
            self.snake[k].goto(xc, lc)
        self.snake[0].fd(10)

    def snake_controls(self):
        self.screen.onkey(self.up, "Up")
        self.screen.onkey(self.down, "Down")
        self.screen.onkey(self.left, "Left")
        self.screen.onkey(self.right, "Right")