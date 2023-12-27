import turtle as t
class Tim(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def reset_position(self):
        self.goto(0,-280)

    def move(self):
        self.forward(10)
