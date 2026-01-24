from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# made the use of the Snake class
snake = Snake()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)               #used the time
    snake.move()

screen.exitonclick()

# ----------------------------------

#                     #   0        1        2
# starting_positions = [(0, 0),(-20, 0), (-40, 0)]
#
# segments = []
#
# # it's just the same thing to be considered
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)



# ---------------------------------
#     for seg_num in range(len(segments) -1, 0, -1):
#         new_x = segments[seg_num - 1].xcor()       #segments[3-1].xcor()  -->   segments[2].xcor()
#         new_y = segments[seg_num - 1].ycor()
#         segments[seg_num].goto(new_x, new_y)
#     segments[0].forward(20)

# ---------------------------------

# segment_1 = Turtle("square")
# segment_2 = Turtle("square")
# segment_3 = Turtle("square")
#
# segment_1.color("white")
# segment_2.color("white")
# segment_3.color("white")
#
# segment_1.goto(0,0)
# segment_2.goto(-20,0)
# segment_3.goto(-40,0)
