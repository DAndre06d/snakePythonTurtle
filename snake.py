from turtle import Turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        """Create the snake"""
        for pos in START_POS:
            self.add_segment(pos)

    def move(self):
        """automatically moves the snake forward by sending the last piece into the next piece position"""
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_left(self):
        """Turn the snake to the left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def add_segment(self, pos):
        snek = Turtle("square")
        snek.penup()
        snek.color("white")
        snek.goto(pos)
        self.segment.append(snek)

    # def reset(self):
    #     for seg in self.segment:
    #         seg.goto(1000,1000)
    #     self.create_snake()
    #     self.head = self.segment[0]
