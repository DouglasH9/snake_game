from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.x_starting_position = 0
        self.segments_list = []
        self.create_snake()
        self.head = self.segments_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        for segment in self.segments_list:
            segment.goto(x=self.x_starting_position, y=0)
            self.x_starting_position -= 20

    def add_segment(self, position):
        segment = Turtle()
        segment.penup()
        segment.shape("square")
        segment.color("white")
        segment.goto(position)
        self.segments_list.append(segment)

    def extend(self):
        self.add_segment(position=self.segments_list[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.segments_list) - 1, 0, -1):
            new_x = self.segments_list[seg_num - 1].xcor()
            new_y = self.segments_list[seg_num - 1].ycor()
            self.segments_list[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)
