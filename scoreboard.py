from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("#FFB000")
        self.goto((0, 275))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.color("#FFCC00")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 25, "bold"))
        self.goto(0, -25)
        self.write(f"Your score: {self.score}", align="center", font=("Arial", 20, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
