from turtle import Turtle


def border_create():
    border = Turtle()
    border.hideturtle()
    border.color("white")
    border.penup()
    border.goto(x=-180, y=-220)
    border.pendown()
    border.goto(x=180, y=-220)
    border.goto(x=180, y=220)
    border.goto(x=-180, y=220)
    border.goto(x=-180, y=-220)


class Bricks:

    def __init__(self):
        border_create()
        self.FONT = ("Arial", 14, "normal")
        self.level = Turtle()
        self.level_config()
        self.x_pos = [-160, -120, -80, -40, 0, 40, 80, 120, 160]
        self.y_pos = [-200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200]
        self.groups = []
        self.num_of_bricks = 3
        for _ in range(0, 11):
            self.group_create()
        for x in range(0, 3):
            self.groups[0][x].goto(x=self.x_pos[x], y=self.y_pos[0])
        for y in range(1, 11):
            for x in range(0, 3):
                self.groups[y][x].goto(x=-1000, y=self.y_pos[y])

    def group_create(self):
        bricks = [Turtle(shape="square") for _ in range(0, 3)]
        for x in range(0, 3):
            bricks[x].color("white", "red")
            bricks[x].penup()
            bricks[x].shapesize(stretch_wid=2, stretch_len=2)
        self.groups.append(bricks)

    def move(self, stage):
        if self.num_of_bricks == 3:
            for x in range(0, 3):
                if self.x_pos[x] <= self.groups[stage][x].xcor() <= self.x_pos[x+6]:
                    self.groups[stage][x].fd(40)
                if self.groups[stage][x].xcor() == self.x_pos[x] or self.groups[stage][x].xcor() == self.x_pos[x+6]:
                    self.groups[stage][x].right(180)
        elif self.num_of_bricks == 2:
            for x in range(0, 2):
                if self.x_pos[x] <= self.groups[stage][x].xcor() <= self.x_pos[x + 7]:
                    self.groups[stage][x].fd(40)
                if self.groups[stage][x].xcor() == self.x_pos[x] or self.groups[stage][x].xcor() == self.x_pos[x + 7]:
                    self.groups[stage][x].right(180)
        elif self.num_of_bricks == 1:
            for x in range(0, 1):
                if self.x_pos[x] <= self.groups[stage][x].xcor() <= self.x_pos[x + 8]:
                    self.groups[stage][x].fd(40)
                if self.groups[stage][x].xcor() == self.x_pos[x] or self.groups[stage][x].xcor() == self.x_pos[x + 8]:
                    self.groups[stage][x].right(180)

    def check_fall(self, stage):
        if 0 < stage < 12:
            for brick in range(0, 3):
                if self.groups[stage][brick].xcor() != self.groups[stage-1][0].xcor() and self.groups[stage][brick].xcor() != self.groups[stage-1][1].xcor() and self.groups[stage][brick].xcor() != self.groups[stage-1][2].xcor():
                    self.groups[stage][brick].goto(x=-1000, y=0)
                    self.num_of_bricks -= 1

    def level_config(self):
        self.level.hideturtle()
        self.level.penup()
        self.level.color("White")
        self.level.goto(x=-20, y=240)
        self.level.write("Level: 0", font=self.FONT)
