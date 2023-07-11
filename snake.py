from turtle import Screen, Turtle
Move_Forward = 20
Starting_Pos = [(0, 0), (-20, 0), (-40, 0)]
Up = 90
Down = 270
Left = 180
Right = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in Starting_Pos:
            self.add_segment(i)

    def add_segment(self, i):
        shrey = Turtle("square")
        shrey.color("#33FF00")
        shrey.penup()
        shrey.goto(i)
        self.segments.append(shrey)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].fd(Move_Forward)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)