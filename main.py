import time
from turtle import Screen
from main_body import Bricks

SP_1 = 0.05125
SP_2 = 0.125
SP_3 = 0.25
SP_4 = 0.5
time_stage = [SP_4, SP_4, SP_4, SP_3, SP_3, SP_3, SP_2, SP_2, SP_2, SP_1, SP_1]
stage = 0

root = Screen()
root.setup(height=600, width=500)
root.title("Bricks")
root.bgcolor("black")
root.listen()
root.tracer(0)


def deploy():
    global stage
    bricks.check_fall(stage=stage)
    stage += 1
    if stage < 11:
        for x in range(0, bricks.num_of_bricks):
            bricks.groups[stage][x].goto(x=bricks.x_pos[x], y=bricks.y_pos[stage])


bricks = Bricks()

while stage < 11 and bricks.num_of_bricks > 0:
    time.sleep(time_stage[stage])
    bricks.move(stage=stage)
    root.onkeypress(key="space", fun=deploy)
    root.update()

if bricks.num_of_bricks > 0:
    print("You win!")
else:
    print("Game over")

root.mainloop()
