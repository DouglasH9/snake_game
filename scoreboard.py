from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Roboto Mono", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.goto(0, 350)
        self.score = 0
        self.shape("classic")
        self.color("White")
        self.update_board()
        self.hideturtle()

    def update_board(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
