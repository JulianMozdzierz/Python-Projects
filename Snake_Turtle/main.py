import time, turtle
from food import *
from snake import *


win = turtle.Screen()
win.title("Snake Game")
width = 500
height = 500
win.setup(width=width, height= height)
win.bgcolor("green")

snake = Snake(0, 0)
win.listen()
win.onkey(snake.keyUp, "Up")
win.onkey(snake.keyDown, "Down")
win.onkey(snake.keyRight, "Right")
win.onkey(snake.keyLeft, "Left")

win.onkey(snake.keyUp, "w")
win.onkey(snake.keyDown, "s")
win.onkey(snake.keyRight, "d")
win.onkey(snake.keyLeft, "a")


food = Food()

while True:
    win.update()
    time.sleep(0.1)
    snake.snakeMove()

    if snake.head.distance(food) < 20: 
        food.Refresh()
        snake.extend()

    if snake.checkSelfCollisions() or snake.checkWallsColision(width, height):
        food.Refresh()
        snake.Refresh()

win.turtle.mainloop()