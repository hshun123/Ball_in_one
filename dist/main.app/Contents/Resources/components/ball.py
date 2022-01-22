import pygame
import pymunk
import random
import components.colors as colors
import components.func as fc

class Ball():
    def __init__(self,space, x, y, collision_type, up = 1):
        self.body = pymunk.Body()
        self.body.position = [x, y]
        self.body.velocity = [0,0]
        # self.body.velocity = 0, up * 100
        self.shape = pymunk.Circle(self.body, 10)
        self.shape.elasticity = 1
        self.shape.density = 1
        self.shape.friction = 1
        self.shape.mass = 10
        self.shape.collision_type = collision_type

        # # ball 
        # self.main_ball = Ball(space, 40.0, 775.0, 1, 1)
        space.add(self.body, self.shape)

        self.end = False
        self.ball_img = pygame.image.load(r'images/ball_red_small.png')
        # space.add(self.body, self.shape)

    def update(self, screen):
        # draw the ball
        # pygame.draw.circle(screen, colors.ORANGE, (self.body.position[0], self.body.position[1]), 10)
        scaled_img = pygame.transform.scale(self.ball_img, (20,20))
        rec = scaled_img.get_rect(center = self.body.position)
        screen.blit(scaled_img, rec)

    def drag_mouse_vel(self, space, mouse_up_pos, mouse_down_pos):
        # when the user drag and realease the mouse click
        # calculate the related velocity of the drag

        # if mouse_up_pos != (0,0) and mouse_down_pos != (0,0) and mouse_drag == True:
        if mouse_up_pos != (0,0) and mouse_down_pos != (0,0):
            new_vel = fc.tup_sub(mouse_up_pos, mouse_down_pos)
            self.body.velocity = [new_vel[0], new_vel[1]]
            # update the ball position using the drag velocity
            self.body.position = [(self.body.position[0] + self.body.velocity[0] * 0.02), (self.body.position[1] + self.body.velocity[1] * 0.02)]
            return True

    def collide_bottom(self, arbiter, space, data):
        # self.shape.collision_type = 2
        self.end = True
        print("Hit the bottom")