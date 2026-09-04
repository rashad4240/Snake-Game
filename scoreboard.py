from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")

ALIGNMENT_H_S = "right"
FONT_H_S = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        # Score setup
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.updated_score()

        # High Score Turtle setup
        self.high_score_turtle = Turtle()
        self.high_score_turtle.color("white")
        self.high_score_turtle.penup()
        self.high_score_turtle.hideturtle()
        self.update_high_score()

    def updated_score(self):
        self.clear()
        self.goto(-250, 270)
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)

    def update_high_score(self):
        self.high_score_turtle.clear()
        self.high_score_turtle.goto(200, 270)
        self.high_score_turtle.write(f"High Score: {self.high_score}",align=ALIGNMENT_H_S,font=FONT_H_S)

    def increase_score(self):
        self.score += 1
        self.updated_score()

        # Check if current score is greater than high score
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()

            with open("data.txt", "w") as file:
                file.write(str(self.high_score))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over",align=ALIGNMENT,font=FONT)