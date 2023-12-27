import turtle as t
import random
COLORS=["orange","black","yellow","purple","blue","green","red"]
MOVE_DISTANCE=5
class Cars:
    def __init__(self):
        self.cars=[]
        self.speed=MOVE_DISTANCE
    def create_cars(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            car=t.Turtle("square")
            car.shapesize(1,2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(400,random.randint(-240,240))
            self.cars.append(car)
    def move_cars(self):
        for car in self.cars:
            car.backward(self.speed)
    def levelup(self):
        self.speed+=3
