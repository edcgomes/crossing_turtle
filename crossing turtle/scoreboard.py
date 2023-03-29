from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.number = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-220, 260)

    def track_score(self):
        self.clear()
        self.write(f"Level: {self.number}", False, "center", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)
