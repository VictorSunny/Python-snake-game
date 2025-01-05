from turtle import Turtle as t
class Scoreboard(t):
    score = 0
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.write(f"Score: {Scoreboard.score}", False)

    def renew(self):
        self.clear()
        Scoreboard.score += 1
        self.write(f"Score: {Scoreboard.score}", False)

    def fail(self):
        self.color("white")
        self.turtlesize(20)
        self.write("GAME OVER!")


