import pygame
import pymunk
import random
from components.ball import Ball
import components.colors as colors
import components.func as fc


class Main_Ball():
    def __init__(self, space):
        # # ball 
        self.main_ball = Ball(40.0, 775.0, 1, 1)
        space.add(self.main_ball.body, self.main_ball.shape)


    def update(self, screen):
        # draw the ball
        pygame.draw.circle(screen, colors.ORANGE, (self.main_ball.body.position[0], self.main_ball.body.position[1]), 10)

    def drag_mouse_vel(self, space, mouse_up_pos, mouse_down_pos):
        # when the user drag and realease the mouse click
        # calculate the related velocity of the drag

        # if mouse_up_pos != (0,0) and mouse_down_pos != (0,0) and mouse_drag == True:
        if mouse_up_pos != (0,0) and mouse_down_pos != (0,0):
            new_vel = fc.tup_sub(mouse_up_pos, mouse_down_pos)
            self.main_ball.body.velocity = [new_vel[0], new_vel[1]]
            # update the ball position using the drag velocity
            self.main_ball.body.position = [(self.main_ball.body.position[0] + self.main_ball.body.velocity[0] * 0.01), (self.main_ball.body.position[1] + self.main_ball.body.velocity[1] * 0.01)]
            return True