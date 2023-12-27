from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level=1
        self.penup()
        self.writelevel()
    def writelevel(self):
        self.clear()
        self.goto(-350,270)
        self.hideturtle()
        self.write(f"Level : {self.current_level}",False,"left",("Courier",16,"normal"))
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over",False,"center",("Courier",16,"normal"))