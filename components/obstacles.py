from tkinter import W
import pygame
import pymunk
import random
import math
import components.func as fc

class Obsticle():
    def __init__(self, x, y, w, h, a, collision_type):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = [x, y]
        self.body.angle = math.radians(a)

        self.shape = pymunk.Poly.create_box(self.body,(w,h))
        self.shape.elasticity = 1
        self.shape.collision_type = collision_type

    def scale_back(self, scale_x, scale_y,  img:pygame.Surface):
        img_size = img.get_size()
        transformed_img = pygame.transform.scale(img, (scale_x, scale_y))
        res = [self.body.position[0], self.body.position[1] - img_size[1] * 1]
        return res

    def rotate_img(self):
        pass

    def draw(self):
        pass