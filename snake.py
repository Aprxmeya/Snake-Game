import turtle

from turtle import Turtle

POSITION = [(0,0),(-20,0),(-40,0)]
DISTANCE = 20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for i in POSITION:
            self.add_part(i)

    def add_part(self,i):
        part = Turtle(shape="square")
        part.color("white")
        part.penup()
        part.goto(i)
        self.parts.append(part)

    def extend(self):#adds to the last part to the list auto travels behind the -2 since no pause
        self.add_part(self.parts[-1].position())

    def move(self):
        for part in range(len(self.parts)-1, 0, -1):
            new_x_coordinate = self.parts[part - 1].xcor()
            new_y_coordinate = self.parts[part - 1].ycor()
            self.parts[part].goto(new_x_coordinate, new_y_coordinate)
        self.head.forward(DISTANCE)
            # self.parts[0].left(80)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    #below border line is not Acurrate dont trust it blindly
    def createborder(self):
        border = Turtle()
        border.color("white")
        border.penup()
        border.hideturtle()
        border.goto(280,0)  #move right and then move for motion
        border.speed("fastest")
        # Draw the square border
        border.pendown()
        border.left(90)
        border.forward(280)
        border.left(90)
        border.forward(560)
        border.left(90)
        border.forward(560)
        border.left(90)
        border.forward(560)
        border.left(90)
        border.forward(280)


