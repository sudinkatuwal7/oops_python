from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # segments[3-1].xcor()  -->   segments[2].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
             self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
             self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
             self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)



# Good to know,
# self.segments[0].setx(self.segments[0].xcor() + MOVE_DISTANCE)
# Purpose: Move the snake head to the right

# self.segments[0].sety(self.segments[0].ycor() + MOVE_DISTANCE)
# Purpose: Move the snake head upward

# self.segments[0].setx(self.segments[0].xcor() - MOVE_DISTANCE)
# Purpose: Move the snake head to the left

# self.segments[0].sety(self.segments[0].ycor() - MOVE_DISTANCE)
# Purpose: Move the snake head downward


