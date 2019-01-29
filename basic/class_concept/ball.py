#!/usr/bin/python
# -*- coding: UTF-8 -*-


class ball(object):
    def __init__(self):
        self.direction = 'down'
        self.color = 'red'
        self.size = 'small'

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"


myball = ball()
# myball.direction = "down"
# myball.color = "green"
# myball.size = "small"

print("I just created a ball")
print("my ball is", myball.size)
print("my ball is", myball.color)
print("my ball's direction is", myball.direction)
print("now i'm going to bounce the ball")
#print
print(myball.bounce())
