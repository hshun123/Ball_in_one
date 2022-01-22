import pygame
import pymunk
import random


# Wall class 
class Wall():
    def __init__(self, x1, y1, x2, y2, collision_type, radius = 10):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, (x1, y1), (x2, y2), radius)
        self.shape.elasticity = 0.4
        #
        self.shape.friction = 100

    def collide(self, arbiter, space, data):
        # self.shape.collision_type = 2
        pass