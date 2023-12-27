from turtle import Screen,Turtle
from player import Tim
from vehicles import Cars
from scoreboard import ScoreBoard
import time
screen=Screen()
screen.setup(800,600)
screen.tracer(0)
screen.listen()
sign=Turtle()
sign.pencolor("black")
sign.penup()
sign.goto(400,260)
sign.pendown()
sign.goto(-400,260)
sign.penup()
sign.goto(-400,-260)
sign.pendown()
sign.goto(400,-260)
player=Tim()
npc_cars=Cars()
score=ScoreBoard()
screen.onkey(player.move,"Up")
screen.title("Tim crossing road")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    npc_cars.create_cars()
    npc_cars.move_cars()
    if player.ycor()>=270:
        player.reset_position()
        score.current_level+=1
        score.writelevel()
        npc_cars.levelup()
    for car in npc_cars.cars:
        if player.distance(car)<10:
            game_is_on=False
            score.gameover()
screen.exitonclick()