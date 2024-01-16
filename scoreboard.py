from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("myFile.txt", mode="r") as file:
            self.highest_score = int(file.read())
        self.writes()

    def writes(self):
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("myFile.txt", mode="w") as file:
                file.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



