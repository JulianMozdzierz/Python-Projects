from turtle import Turtle
import random 


class Food(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.Refresh()

    def Refresh(self):
        color = random.choice(["blue", "yellow", "red"])
        shape = random.choice(["square", "circle", "triangle"])
        self.hideturtle()
        self.color(color)
        self.shape(shape)
        self.goto(random.randint(-200,200), random.randint(-200, 200))
        self.showturtle()