import pygame
import pymunk
import random
import math
import components.func as fc

class Brick():
    def __init__(self, x, y, w, h, a, collision_type):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = [x, y]
        self.body.angle = math.radians(a)
        # self.body.velocity = 0, up * 100
        vs = [(w/2,-h/2), (w/2,h/2), (-w/2,h/2)]
        self.shape = pymunk.Poly(self.body, vs, None, 0)
        self.shape.elasticity = 1
        self.shape.collision_type = collision_type 

    def collide(self, arbiter, space, data):
        pass

    def scale_back(self, img:pygame.Surface):
        img_size = img.get_size()
        res = [self.body.position[0] - img_size[0] * 0.5, self.body.position[1] - img_size[1] * 0.5]
        return res

    def rotate_img(self):
        pass

    def draw(self):
        pass