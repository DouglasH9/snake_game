from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Roboto Mono", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.goto(0, 350)
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.shape("classic")
        self.color("White")
        self.update_board()
        self.hideturtle()

    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_board()
